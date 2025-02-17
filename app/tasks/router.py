from typing import Optional, Union

from fastapi import APIRouter, Depends

from app.tasks.dao import TaskDAO
from app.tasks.schemas import STask, STaskAdd, STaskUpd
from app.tasks.request_body import RBTask


router = APIRouter(prefix='/tasks', tags=['Work with tasks'])


@router.get('', summary='Get all tasks')
async def get_all_tasks(request_body: RBTask = Depends()) -> list[STask]:
    return await TaskDAO.find_all_full(**request_body.to_dict())


@router.get('/one', summary='Get one task or none by filters')
async def get_one_or_none_task_by_filter(request_body: RBTask = Depends()) -> Union[STask, dict]:
    result = await TaskDAO.find_one_or_none_full(**request_body.to_dict())
    return result if result is not None else {'message': 'Task with given filters is not found!',
                                              'filters': request_body.to_dict()}


@router.get('/{task_id}', summary='Get one task or none by id')
async def get_one_or_none_task_by_id(task_id: int) -> Union[STask, dict]:
    result = await TaskDAO.find_one_or_none_full(id=task_id)
    return result if result is not None else {'message': f'Task with id \'{task_id}\' is not found!'}


@router.post('/add', summary='Add new task in database')
async def add_task(task: STaskAdd) -> dict:
    new_task = await TaskDAO.add(**task.model_dump())
    if new_task:
        return {'message': 'Task is added successfully!', 'task': new_task.to_dict()}
    else:
        return {'message': 'Error while adding new task!'}


@router.put('/update-one', summary='Update a task by id')
async def update_task(task: STaskUpd) -> dict:
    affected_rows = await TaskDAO.update(filter_by={'id': task.id}, **task.model_dump(exclude={'id'}))
    if affected_rows:
        return {'message': f'Task with id \'{task.id}\' is updated successfully!', 'task': task}
    else:
        return {'message': f'Error while updating task with id \'{task.id}\'!'}


@router.delete("/delete/{task_id}")
async def delete_task(task_id: int) -> dict:
    affected_rows = await TaskDAO.delete(id=task_id)
    if affected_rows:
        return {'message': f'Task with id \'{task_id}\' is deleted!'}
    else:
        return {'message': f'Error while deleting task with id \'{task_id}\'!'}
