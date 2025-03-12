from typing import Optional, Union
from datetime import date


class RBTask:
    def __init__(self, task_id: Optional[int] = None,
                 name: Optional[str] = None,
                 parent_tasks: Optional[str] = None,
                 child_tasks: Optional[str] = None,
                 employee_id: Optional[Union[int, str]] = None,
                 deadline: Optional[Union[date, str]] = None,
                 status: Optional[str] = None):
        self.id: Optional[int] = task_id
        self.name: Optional[str] = name
        self.parent_tasks: Optional[Union[list[int], str]] = self.__to_list(parent_tasks)
        self.child_tasks: Optional[Union[list[int], str]] = self.__to_list(child_tasks)
        self.employee_id: Optional[Union[int, str]] = employee_id
        self.deadline: Optional[Union[date, str]] = deadline
        self.status: Optional[str] = status

    def to_dict(self) -> dict:
        obj_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, str) and value.lower() in ['none', 'null']:
                obj_dict[key] = None
            elif value is not None:
                obj_dict[key] = value
        return obj_dict

    @staticmethod
    def __to_list(string: Optional[str]) -> Optional[Union[list[int], str]]:
        if string:
            if string.lower() in ['none', 'null']:
                return string

            res_list: list[int] = []
            for item in string.split(','):
                try:
                    item = int(item.strip())
                except ValueError:
                    raise ValueError(f'"{item}" is not int, so it can\'t be an ID for IDs list filter')
                res_list.append(item)

            return res_list

        return None
