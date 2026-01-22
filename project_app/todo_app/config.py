import os

class Config:
    """Configuration class for application settings."""

    PORT = os.environ.get('PORT', 8080)