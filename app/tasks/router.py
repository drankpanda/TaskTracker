from typing import Optional, Union

from fastapi import APIRouter, Depends

from app.tasks.dao import TaskDAO
from app.tasks.schemas import STask
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
