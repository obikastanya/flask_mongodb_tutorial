from flask import Flask, jsonify
from db import Connection

from uuid import uuid1
from flask import request

app=Flask(__name__)
db=Connection('flask_mongo_crud')

@app.get("/users")
def get_users():
    users=db.user.find({})
    return {
        "data": list(users)
    }

@app.get("/user/<user_id>/")
def get_user(user_id):
    query={
        "_id":user_id
    }
    user=db.user.find_one(query)

    if not user:
        return {
            "message":"User is not found"
        }

    return {
        "data":user
    }

@app.delete("/user/<user_id>/")
def delete_user(user_id):
    query={
        "_id":user_id
    }
    result=db.user.delete_one(query)
    
    if not result.deleted_count:
        return {
            "message":"Failed to delete"
        }
    
    return {"message":"Delete success"}

@app.post("/user")
def insert_user():

    _id=str(uuid1().hex)
    
    content=dict(request.json)
    content.update({ "_id":_id })
    
    result =db.user.insert_one(content)
    if not result.inserted_id:
        return {"message":"Failed to insert"}
    
    return {
        "message":"Success", 
        "data":{
            "id":result.inserted_id
            }
        }

@app.put("/user/<user_id>/")
def update_user(user_id):
    filter={
        "_id":user_id
    }
    content=dict(request.json)
    query_update={ "$set": content }
    result=db.user.update_one(filter, query_update)

    if not result.matched_count:
        return {
            "message":"Failed to update. Record is not found"
        }
    
    if not result.modified_count:
        return {
            "message":"No changes applied"
        }
    
    return {"message":"Update success"}

if __name__=="__main__":
    app.run(port=8887, debug=True)