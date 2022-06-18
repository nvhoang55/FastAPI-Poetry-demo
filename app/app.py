from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.router.security import security
from app.router.test import test_route
from app.router.ui import ui_route
from app.router.user import user_route

app = FastAPI()

app.mount("static", StaticFiles(directory="app/static"), name="static")

app.include_router(test_route)
app.include_router(security)
app.include_router(ui_route)
app.include_router(user_route)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
