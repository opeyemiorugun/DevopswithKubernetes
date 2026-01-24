from app import app
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import insert
import os


# Connect to database and run this
postgres_url = os.getenv("POSTGRES_URL")
engine = sa.create_engine(postgres_url)
metadata = sa.MetaData()
pingpong = sa.Table(
    'pingpong',
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column('pings', sa.Integer, nullable=False)
)
metadata.create_all(engine)


def retrieve_counter():
    with engine.connect() as conn:
        result = conn.execute(sa.select(pingpong.c.pings).where(pingpong.c.id == 1)).scalar_one_or_none()
        counter = result if result is not None else 0
    return counter

@app.route('/')
def index(): 
    with engine.begin() as conn:
        result = conn.execute(insert(pingpong).values(
            id=1,
            pings=1
        ).on_conflict_do_update(
            index_elements=["id"],
            set_={"pings": pingpong.c.pings + 1}
        ).returning(pingpong.c.pings)).scalar_one()
    return f'pong {result}'

@app.route('/pings')
def pings():
    counter = retrieve_counter()
    return {'pings': counter}, 200