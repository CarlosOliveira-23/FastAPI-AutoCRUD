from fastapi import FastAPI
from app.routes import user_router, product_router

app = FastAPI(title="Gerador de API REST Automática", version="1.0")

app.include_router(user_router)
app.include_router(product_router)


@app.get("/")
async def root():
    return {"message": "API REST Automática gerada com sucesso!"}
