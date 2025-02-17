from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class STask(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str = Field(..., description='Name of the task')
    parent_task: Optional[int] = Field(None, description='ID of the parent task')
    employee_id: Optional[int] = Field(None, description='ID of the assignee')
    employee: Optional[str] = Field(None, description='Full name of the assignee')
    deadline: Optional[date] = Field(None, description='Expiration date of the task')
    status: Optional[str] = Field(None, description='Status of the task')
    created_at: datetime = Field(..., description='Timestamp of the creation')
    updated_at: datetime = Field(..., description='Timestamp of last update')
