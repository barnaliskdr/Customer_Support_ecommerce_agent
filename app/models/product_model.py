from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from utils.objectid_util import PyObjectId

class Product(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str
    category: str
    price: float
    portion: str
    image: str
    description: str

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
