from typing import Optional

from sqlalchemy import select, and_, Select
from sqlalchemy.orm import joinedload, selectinload

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
        async with (async_session_maker() as session):
            query = (
                select(cls.model)
                .options(joinedload(cls.model.employee))
                .options(selectinload(cls.model.parent_tasks))
                .options(selectinload(cls.model.child_tasks))
            )
            query = await cls._family_filter(query, **filter_by)
            result = await session.execute(query)
            task = result.scalar_one_or_none()

            if task is None:
                return None

            task_full_info = task.to_dict()
            task_full_info['parent_tasks'] = task.to_ids_names_dicts(task.parent_tasks)
            task_full_info['child_tasks'] = task.to_ids_names_dicts(task.child_tasks)
            task_full_info['employee'] = (
                task.employee.first_name + ' ' + task.employee.last_name if task_full_info['employee_id'] else None
            )
            return task_full_info

    @classmethod
    async def find_all_full(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .options(joinedload(cls.model.employee))
                .options(selectinload(cls.model.parent_tasks))
                .options(selectinload(cls.model.child_tasks))
            )
            query = await cls._family_filter(query, **filter_by)
            result = await session.execute(query)
            tasks = result.scalars().all()

            tasks_full_info = []
            for task in tasks:
                task_full_info = task.to_dict()
                task_full_info['parent_tasks'] = task.to_ids_names_dicts(task.parent_tasks)
                task_full_info['child_tasks'] = task.to_ids_names_dicts(task.child_tasks)
                task_full_info['employee'] = (
                    task.employee.first_name + ' ' + task.employee.last_name if task_full_info['employee_id'] else None
                )
                tasks_full_info.append(task_full_info)

            return tasks_full_info

    @classmethod
    async def _family_filter(cls, query: Select, **filter_by) -> Select:
        if 'parent_tasks' in filter_by:
            parent_tasks: Optional[list[int]] = filter_by.get('parent_tasks')
            if parent_tasks:
                filter_by.pop('parent_tasks')
                query = query.filter(and_(*[cls.model.parent_tasks.any(id=task_id) for task_id in parent_tasks]))

        if 'child_tasks' in filter_by:
            child_tasks: Optional[list[int]] = filter_by.get('child_tasks')
            if child_tasks:
                filter_by.pop('child_tasks')
                query = query.filter(and_(*[cls.model.child_tasks.any(id=task_id) for task_id in child_tasks]))

        query = query.filter_by(**filter_by)

        return query
