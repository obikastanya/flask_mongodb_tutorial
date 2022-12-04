from flask import (
    Flask, 
    request
)
from db import Connection

app=Flask(__name__)
db=Connection('flask_mongo_crud')

# @app.get("/products")
# def get_products():
    
#     aggregate_query=[
#         { '$lookup': {
#             'from': 'product_category', 
#             'localField': 'category', 
#             'foreignField': '_id', 
#             'as': 'category'
#             }
#         }, 
#         {
#         '$unwind': {
#             'path': '$category', 
#             'preserveNullAndEmptyArrays': False
#             }
#         }
#     ]

#     result=db.product.aggregate(aggregate_query)

#     return {
#         "data":list(result)
#     }, 200


@app.get("/products")
def get_products():
    
    aggregate_query=[
        { '$lookup': {
            'from': 'product_category', 
            'localField': 'category', 
            'foreignField': '_id', 
            'as': 'category'
            }
        }, 
        {
        '$unwind': {
            'path': '$category', 
            'preserveNullAndEmptyArrays': False
            }
        }
    ]
    
    category=request.args.get("category")

    if category:
        aggregate_query.append({
            "$match":{
                "category.description":{
                    "$regex":category, "$options":"i"
                }
            }
        })
    

    result=db.product.aggregate(aggregate_query)

    return {
        "data":list(result)
    }, 200


if __name__=="__main__":
    app.run(debug=True, port=8887)