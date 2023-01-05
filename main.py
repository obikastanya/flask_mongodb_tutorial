from flask import (
    Flask,
    request
)
from uuid import uuid1
from db import Connection

from pymongo.errors import WriteError
from error import SchemaValidationError

app=Flask(__name__)
db=Connection('flask_mongo_crud')


@app.post("/product")
def insert_product():  
    
    content=request.json
    content["_id"]= str( uuid1().hex )
    
    try:
        result = db.product.insert_one(content)
        insert_product=db.product.find_one({"_id":result.inserted_id})

        return {
            "message":"Product successfully inserted",
            "data":insert_product
        }, 200

    except WriteError as e:
        return {
            "message":SchemaValidationError(e)
        }, 500


@app.post("/product-category")
def insert_product_category():  
    
    content=request.json
    content["_id"]= str( uuid1().hex )
    
    try:
        result = db.product_category.insert_one(content)
        insert_product_category=db.product_category.find_one({"_id":result.inserted_id})

        return {
            "message":"Product Category successfully inserted",
            "data":insert_product_category
        }, 200

    except WriteError as e:
        return {
            "message":SchemaValidationError(e)
        }, 500


if __name__=="__main__":
    app.run(port=8887, debug=True)