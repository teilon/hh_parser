import os

from sqlalchemy import create_engine

POSTGRES_HOST = '84.38.181.88' # os.environ['POSTGRES_HOST'] #'78.155.206.12'
POSTGRES_PORT = '5432' # os.environ['POSTGRES_PORT'5432''] #'5432'
POSTGRES_DATABASE = 'geralddb' # os.environ['POSTGRES_DB'] #'postgres_db'
POSTGRES_USER = 'torn' # os.environ['POSTGRES_USER'] #'torn'
POSTGRES_PASSWORD = 'helicopter' # os.environ['POSTGRES_PASSWORD'] #'helicopter'

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.\
    format(POSTGRES_USER,
           POSTGRES_PASSWORD,
           POSTGRES_HOST,
           POSTGRES_PORT,
           POSTGRES_DATABASE)

db = create_engine(SQLALCHEMY_DATABASE_URI, echo = False)