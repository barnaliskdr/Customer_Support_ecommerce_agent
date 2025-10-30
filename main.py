from fastapi import FastAPI
from app.routes import product_routes

app = FastAPI()


app.include_router(product_routes.router)
# app.include_router(user_routes.router)

# @app.get("/")
# async def root():
#     return {"message": "Welcome to the E-commerce API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)