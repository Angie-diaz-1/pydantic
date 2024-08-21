from fastapi import FastAPI

from app.routes import user_routes

app = FastAPI()
#incluir rutas de usuario
app.include_router(user_routes.router
                   , prefix='/users',
                   tags=['Users'])

@app.get("/")
async def root():
    return {"message": "Hello World"}


