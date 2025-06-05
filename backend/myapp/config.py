import os
from pathlib import Path
from dotenv import load_dotenv

# Get absolute path to .env
env_path = Path(__file__).resolve().parent.parent / '.env'
print(f"🔍 Looking for .env at: {env_path}")

# Load environment variables
load_dotenv(env_path, override=True, verbose=True)


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600))
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '').split(',')

    @classmethod
    def check_config(cls):
        required_vars = {
            'SECRET_KEY': cls.SECRET_KEY,
            'DATABASE_URL': cls.SQLALCHEMY_DATABASE_URI,
            'JWT_SECRET_KEY': cls.JWT_SECRET_KEY
        }

        print("\n🔧 Configuration check:")
        for name, value in required_vars.items():
            print(f"{name}: {'✅' if value else '❌'}")
            if not value:
                raise ValueError(f"{name} not loaded from .env file")