from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId


# Utility class to handle MongoDB ObjectId with Pydantic
# app/utils/objectid_util.py

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
