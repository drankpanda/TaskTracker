from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.employees.router import get_all_employees
from app.tasks.router import get_all_tasks

router = APIRouter(prefix='/view', tags=['Frontend'])
templates = Jinja2Templates(directory='app/templates', trim_blocks=True, lstrip_blocks=True)


@router.get('/tasks')
async def get_students_html(request: Request, tasks=Depends(get_all_tasks), employees=Depends(get_all_employees)):
    return templates.TemplateResponse(name='tasks/tasks.html', context={'request': request,
                                                                        'tasks': tasks,
                                                                        'employees': employees})
