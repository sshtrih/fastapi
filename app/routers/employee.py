from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from models.employee import Person, get_db

employee = APIRouter()


@employee.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    return db.query(Person).all()


@employee.get("/employees/{inn}")
def get_employee_by_inn(inn, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.inn == inn).first()
    return person


@employee.post("/employees")
def create_employee(data=Body(), db: Session = Depends(get_db)):
    person = Person(passport_series=data["passport_series"],
                    passport_numbers=data["passport_numbers"],
                    full_name=data["full_name"],
                    post=data["post"],
                    phone_number=data["phone_number"],
                    inn=data["inn"],
                    login=data["login"])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


@employee.delete("/employees")
def delete_employee(inn, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.inn == inn).first()
    db.delete(person)
    db.commit()
