import json
import os
from db import Connection

db=Connection('flask_mongo_crud')

def create_collection(collection_name):
    try:
        db.create_collection(collection_name)
    except:
        print(f"Collection '{collection_name}' already exists")
    else:
        print(f"Collection '{collection_name}' successfully created")

def create_schema_validator(collection_name, validation):
    try:
        db.command(validation)
    except:
        print(f"Failed to create validation for '{collection_name}' collections")
    else:
        print(f"Validation for '{collection_name}' collections successfully created")

def read_json(FILE_DIR):
    file=open(FILE_DIR, "r")
    validation=json.load(file)
    return validation

BASE_DIR=os.getcwd()
SCHEMA_DIR= os.path.join(BASE_DIR, 'schema')

for file_name in os.listdir(SCHEMA_DIR):
    FILE_DIR=os.path.join(SCHEMA_DIR, file_name)
    
    collection_name=file_name.split(".")[0]    
    validation=read_json(FILE_DIR)

    create_collection(collection_name)
    create_schema_validator(collection_name, validation)
