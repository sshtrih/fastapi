from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from config.postgres import engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "employees"

    passport_series = Column(String(4), nullable=False)
    passport_numbers = Column(String(6), nullable=False)
    full_name = Column(String(255), nullable=False)
    post = Column(String(10), nullable=False)
    phone_number = Column(String(11), unique=True)
    inn = Column(String(12), primary_key=True, nullable=False)
    login = Column(String(255), nullable=False, unique=True)


Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
