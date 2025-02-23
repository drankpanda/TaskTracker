from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.tasks.router import get_all_tasks

router = APIRouter(prefix='/view', tags=['Frontend'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/tasks')
async def get_students_html(request: Request, tasks=Depends(get_all_tasks)):
    return templates.TemplateResponse(name='tasks.html', context={'request': request, 'tasks': tasks})
