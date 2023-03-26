from fastapi import FastAPI

from routers.employee import employee
from routers.product import product

app = FastAPI()
app.include_router(product)
app.include_router(employee)

