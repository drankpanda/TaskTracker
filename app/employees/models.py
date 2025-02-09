from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from app.database import BaseTable, int_pk, str_null_true
if TYPE_CHECKING:
    from app.tasks.models import Task


# Create employees table model
class Employee(BaseTable):
    id: Mapped[int_pk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    job: Mapped[str_null_true]

    # One-to-many relationship: one employee can have multiple tasks
    tasks: Mapped[list['Task']] = relationship('Task', back_populates='employee')

    def __str__(self):
        return f'{self.__class__.__name__}(id="{self.id}", name="{self.first_name!r} {self.last_name!r}")'

    def __repr__(self):
        return str(self)
