from typing import Optional


class RBEmployee:
    def __init__(self, employee_id: Optional[int] = None,
                 first_name: Optional[str] = None,
                 last_name: Optional[str] = None,
                 job: Optional[str] = None):
        self.id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.job = job

    def to_dict(self) -> dict:
        obj_dict = {}
        # Need to create a copy (.items()) in order to exclude changes in runtime because of asynchronous work
        for key, value in self.__dict__.items():
            if value in ['None', 'none', 'NONE', 'Null', 'null', 'NULL']:
                obj_dict[key] = None
            elif value is not None:
                obj_dict[key] = value
        return obj_dict
