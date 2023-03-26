import os

from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = 'postgresql://' + os.environ["POSTGRES_USER"] + ':' + os.environ["POSTGRES_PASSWORD"] + \
                          '@postgres:5432/' + os.environ["POSTGRES_DB"]
engine = create_engine(SQLALCHEMY_DATABASE_URL)
