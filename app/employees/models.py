from sqlalchemy.orm import Mapped

from app.database import BaseTable, int_pk, str_null_true


# Create employees table model
class Employee(BaseTable):
    id: Mapped[int_pk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    job: Mapped[str_null_true]

    def __str__(self):
        return f'{self.__class__.__name__}(id="{self.id}", name="{self.first_name!r} {self.last_name!r}")'

    def __repr__(self):
        return str(self)
