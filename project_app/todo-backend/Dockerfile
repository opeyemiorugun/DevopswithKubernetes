FROM python:3.11-slim

WORKDIR /usr/src/project_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

ENTRYPOINT [ "flask" ]

CMD [ "run" , "--host=0.0.0.0" ]