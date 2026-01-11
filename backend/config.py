import os

# Use POSTGRES_HOST from env, default to 'postgres' for Docker Compose
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'postgres')
DATABASE_URL = os.environ.get('DATABASE_URL', POSTGRES_HOST)
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'Docker-Integration-Host')
DATABASE_USER = os.environ.get('DATABASE_USER', 'Admin')
DATABASE_PASS = os.environ.get('DATABASE_PASS', 'Hamsa@2005')
DATABASE_PORT = os.environ.get('DATABASE_PORT', '5432')
