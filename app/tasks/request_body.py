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
        obj_data = {'id': self.id, 'name': self.name, 'parent_task': self.parent_task,
                    'employee_id': self.employee_id, 'deadline': self.deadline, 'status': self.status}
        # Need to create a copy (.items()) in order to exclude changes in runtime because of asynchronous work
        not_none_obj_data = {key: value for key, value in obj_data.items() if value is not None}
        return not_none_obj_data
