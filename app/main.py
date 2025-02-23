from typing import Optional
from random import random

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.tasks.router import router as tasks_router
from app.employees.router import router as employees_router
from app.pages.router import router as pages_router


app: FastAPI = FastAPI()


@app.get('/')
def test_welcome_script(message: Optional[str] = 'Greetings!'):
    return {
        'random_number': int(random()*100),
        'message': message,
    }


@app.get('/favicon.ico')
def get_favicon():
    file_name: str = 'favicon.png'
    file_path: str = f'app\\static\\images\\{file_name}'
    return FileResponse(path=file_path, headers={'Content-Disposition': f'attachment; filename={file_name}'})


app.include_router(tasks_router)
app.include_router(employees_router)
app.include_router(pages_router)
app.mount('/static', StaticFiles(directory='app/static'), 'static')
