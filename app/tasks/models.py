from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import BaseTable, int_pk, str_null_true, int_null_true, date_null_true
if TYPE_CHECKING:
    from app.employees.models import Employee


# Create tasks table model
class Task(BaseTable):
    id: Mapped[int_pk]
    name: Mapped[str]
    parent_task: Mapped[int_null_true]
    employee_id: Mapped[int] = mapped_column(ForeignKey('employees.id'), nullable=True)
    deadline: Mapped[date_null_true]
    status: Mapped[str_null_true]

    # One-to-many relationship: one employee can have multiple tasks
    employee: Mapped['Employee'] = relationship('Employee', back_populates='tasks')

    def __str__(self):
        return f'{self.__class__.__name__}(id="{self.id}", name="{self.name!r}")'

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'parent_task': self.parent_task,
            'employee_id': self.employee_id,
            'deadline': self.deadline,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
