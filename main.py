import uvicorn
from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import EmailStr, BaseModel

from attractions_views import router as attractions_router
from users.views import router as users_router

app = FastAPI()
app.include_router(attractions_router)
app.include_router(users_router)


@app.get("/")
def index():
    return {
        "message": "Hello index!",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
