from app.dao.base import BaseDAO
from app.employees.models import Employee
# This import is necessary because SQLAlchemy mapper in runtime needs to
# see Task here because Employee is in relationship with it
from app.tasks.models import Task


class EmployeeDAO(BaseDAO):
    model = Employee
