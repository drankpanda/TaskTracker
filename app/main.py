from typing import Optional
from random import random

from fastapi import FastAPI

from app.tasks.router import router as tasks_router
from app.employees.router import router as employees_router


app = FastAPI()


@app.get('/')
def test_welcome_script(message: Optional[str] = 'Greetings!'):
    return {
        'random_number': int(random()*100),
        'message': message,
    }

app.include_router(tasks_router)
app.include_router(employees_router)
