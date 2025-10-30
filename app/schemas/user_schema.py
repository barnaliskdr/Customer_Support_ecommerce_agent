# ✅ Importing BaseModel and Field from Pydantic
# BaseModel → the foundation for data validation & serialization.
# Field → used to provide extra information like description, default values, etc.
from pydantic import BaseModel, Field

# ✅ Importing Optional from typing module
# Optional[T] means this field can either be of type T or None (missing).
from typing import Optional

# ✅ Importing PyObjectId (custom helper to handle MongoDB ObjectIds)
# This helps FastAPI & Pydantic convert MongoDB’s ObjectId (which is not JSON serializable)
# into a readable string format for API responses.
from utils.objectid_util import PyObjectId


# -------------------------------------------------------------
# 🧱 Base Schema
# -------------------------------------------------------------
# ✅ This is the base schema — it defines the core fields for a user.
# Other schemas like UserCreate or UserUpdate will inherit from this.
class UserBase(BaseModel):
    username: str = Field(..., description="The name of the user")  
    email: str = Field(..., description="User's email address")  
    address: str = Field(..., description="User's residential or delivery address")  
    phone: str = Field(..., description="User's contact phone number")  

    # ✅ The triple dots (...) mean this field is *required*
    # e.g., username: str = Field(...), means username cannot be missing.


# -------------------------------------------------------------
# 🟢 Schema for creating a new user (Client → Server)
# -------------------------------------------------------------
# ✅ This schema is used when a new user registers.
# It includes all required user fields, plus password for registration.
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="User's password (should be stored hashed)")  


# -------------------------------------------------------------
# 🟡 Schema for updating existing user data (Client → Server)
# -------------------------------------------------------------
# ✅ This schema allows partial updates — so all fields are optional.
# For example, the user can update only their address or phone.
class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, description="Updated username")
    email: Optional[str] = Field(None, description="Updated email address")
    password: Optional[str] = Field(None, min_length=6, description="Updated password (hashed)")
    address: Optional[str] = Field(None, description="Updated address")
    phone: Optional[str] = Field(None, description="Updated phone number")


# -------------------------------------------------------------
# 🔵 Schema for reading user data (Server → Client)
# -------------------------------------------------------------
# ✅ This schema is used when sending data *from server to frontend*
# It includes the MongoDB `_id` field, converted to string.
class UserResponse(UserBase):
    # MongoDB automatically creates `_id`, we expose it as `id` here.
    id: Optional[PyObjectId] = Field(alias="_id")

    class Config:
        # ✅ Allows both “id” and “_id” field names to be recognized
        allow_population_by_field_name = True
        
        # ✅ Converts ObjectId → str when returning JSON
        json_encoders = {PyObjectId: str}
        
        # ✅ orm_mode=True allows reading data from ORM-like objects (like MongoDB docs)
        orm_mode = True
