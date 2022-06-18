from fastapi import APIRouter, Request, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

users = [{'id': 1, 'name': "Hoang", 'phone': '1111', 'email': '111@gg.com'},
             {'id': 2, 'name': "Hoang", 'phone': '2222', 'email': '11221@gg.com'},
             {'id': 3, 'name': "Hoang_2", 'phone': '1111', 'email': '111@gg.com'}]

ui_route = APIRouter(
    prefix="/ui"
)

templates = Jinja2Templates(directory="templates")


@ui_route.get("/", response_class=HTMLResponse)
async def ui(request: Request):
    return templates.TemplateResponse("repository.html", {"request": request, 'users': users})


@ui_route.post("/", response_class=HTMLResponse)
async def get_by_id(request: Request, name: str = Form(default="")):

    result = []
    for user in users:
        if user['name'] == name:
            result.append(user)

    return templates.TemplateResponse("repository.html", {"request": request, "result": result})
