from typing import TYPE_CHECKING

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import BaseTable, int_pk, str_null_true, date_null_true
if TYPE_CHECKING:
    from app.employees.models import Employee


# Many-to-many table for tasks
task_to_task = Table(
    'task_to_task',
    BaseTable.metadata,
    Column('parent_task_id', Integer,
           ForeignKey('tasks.id', ondelete='CASCADE'), primary_key=True),
    Column('child_task_id', Integer,
           ForeignKey('tasks.id', ondelete='CASCADE'), primary_key=True),
)


# Create tasks table model
class Task(BaseTable):
    cls_name = 'Task'
    id: Mapped[int_pk]
    name: Mapped[str]
    employee_id: Mapped[int] = mapped_column(ForeignKey('employees.id'), nullable=True)
    deadline: Mapped[date_null_true]
    status: Mapped[str_null_true]

    # One-to-many relationship: one employee can have multiple tasks
    employee: Mapped['Employee'] = relationship('Employee', back_populates='tasks')

    # Many-to-many relationship: one task can have multiple parents and children
    parent_tasks: Mapped[list['Task']] = relationship(
        f'{cls_name}',
        secondary=task_to_task,
        primaryjoin=f'{cls_name}.id==task_to_task.c.child_task_id',
        secondaryjoin=f'{cls_name}.id==task_to_task.c.parent_task_id',
        back_populates='child_tasks'
    )
    child_tasks: Mapped[list['Task']] = relationship(
        f'{cls_name}',
        secondary=task_to_task,
        primaryjoin=f'{cls_name}.id==task_to_task.c.parent_task_id',
        secondaryjoin=f'{cls_name}.id==task_to_task.c.child_task_id',
        back_populates='parent_tasks'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'employee_id': self.employee_id,
            'deadline': self.deadline,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    @staticmethod
    def to_ids_names_dicts(tasks: list['Task']) -> list[dict[str, str]]:
        return [{'id': task.id, 'name': task.name} for task in tasks]

    def __str__(self):
        return f'{self.__class__.__name__}(id="{self.id}", name="{self.name!r}")'

    def __repr__(self):
        return str(self)
