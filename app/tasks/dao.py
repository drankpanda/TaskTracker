from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.tasks.models import Task
# This import is necessary because SQLAlchemy mapper in runtime needs to
# see Employee here because Task is in relationship with it
from app.employees.models import Employee
from app.database import async_session_maker


class TaskDAO(BaseDAO):
    model = Task

    @classmethod
    async def find_one_or_none_full(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.employee)).filter_by(**filter_by)
            result = await session.execute(query)
            task = result.scalar_one_or_none()

            if task is None:
                return None

            task_dict = task.to_dict()
            task_dict['employee'] = None if task_dict['employee_id'] is None else (task.employee.first_name + ' ' +
                                                                                   task.employee.last_name)
            return task_dict

    @classmethod
    async def find_all_full(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.employee)).filter_by(**filter_by)
            result = await session.execute(query)
            tasks = result.scalars().all()

            tasks_full_info = []
            for task in tasks:
                task_dict = task.to_dict()
                task_dict['employee'] = None if task_dict['employee_id'] is None else (task.employee.first_name + ' ' +
                                                                                       task.employee.last_name)
                tasks_full_info.append(task_dict)
            return tasks_full_info
