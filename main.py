from flask import (
    Flask, 
    request
)
from db import Connection

app=Flask(__name__)
db=Connection('flask_mongo_crud')


if __name__=="__main__":
    app.run(debug=True, port=8887)