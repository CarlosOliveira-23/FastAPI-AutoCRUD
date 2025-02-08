from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.user import router as user_router
from app.routes.product import router as product_router

app = FastAPI(
    title="Automatic REST API Generator",
    description="An API that dynamically generates CRUD endpoints based on a PostgreSQL/MySQL database.",
    version="1.0",
    contact={
        "name": "Your Name",
        "email": "your_email@example.com",
        "url": "https://yourwebsite.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(product_router)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "🚀 Automatic REST API Generator is running successfully!"}
