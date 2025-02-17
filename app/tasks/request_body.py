from typing import Optional
from datetime import date


class RBTask:
    def __init__(self, task_id: Optional[int] = None,
                 name: Optional[str] = None,
                 parent_task: Optional[int] = None,
                 employee_id: Optional[int] = None,
                 deadline: Optional[date] = None,
                 status: Optional[str] = None):
        self.id = task_id
        self.name = name
        self.parent_task = parent_task
        self.employee_id = employee_id
        self.deadline = deadline
        self.status = status

    def to_dict(self) -> dict:
        obj_dict = {}
        # Need to create a copy (.items()) in order to exclude changes in runtime because of asynchronous work
        for key, value in self.__dict__.items():
            if value in ['None', 'none', 'NONE', 'Null', 'null', 'NULL']:
                obj_dict[key] = None
            elif value is not None:
                obj_dict[key] = value
        return obj_dict
