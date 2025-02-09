from app.dao.base import BaseDAO
from app.tasks.models import Task
# This import is necessary because SQLAlchemy mapper in runtime needs to
# see Employee here because Task is in relationship with it
from app.employees.models import Employee


class TaskDAO(BaseDAO):
    model = Task
