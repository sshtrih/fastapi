from fastapi import APIRouter
from config.mongodb import conn
from schemas.product import productEntity
from schemas.product import productsEntity
from bson.objectid import ObjectId

from models.product import Product

product = APIRouter()


@product.get('/product')
def find_all_products():
    return productsEntity(conn.hardware_store.products.find())


@product.get('/product/{_id}')
def find_product_by_id(_id: str):
    return productEntity(conn.hardware_store.products.find_one({'_id': ObjectId(_id)}))


@product.post('/product')
def insert_product(_product: Product):
    conn.hardware_store.products.insert_one(dict(_product))


@product.delete('/product')
def remove_product(_id):
    conn.hardware_store.products.delete_one({'_id': ObjectId(_id)})


