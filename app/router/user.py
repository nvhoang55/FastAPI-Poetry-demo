from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.repository.json_db_repository import JsonDBRepository

user_route = APIRouter(
    prefix="/user"
)

templates = Jinja2Templates(directory="templates")

repos = JsonDBRepository()


@user_route.get("/", response_class=HTMLResponse)
async def ui(request: Request):
    users = repos.get_all_users()
    return templates.TemplateResponse("user/index.html", {"request": request, 'users': users})

# @ui_route.post("/", response_class=HTMLResponse)
# async def get_by_id(request: Request, name: str = Form(default="")):
#     result = []
#     for user in users:
#         if user['name'] == name:
#             result.append(user)
#
#     return templates.TemplateResponse("repository.html", {"request": request, "result": result})
