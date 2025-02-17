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


class STaskAdd(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description='Name of the task')
    parent_task: Optional[int] = Field(None, ge=1, description='ID of the parent task')
    employee_id: Optional[int] = Field(None, ge=1, description='ID of the assignee')
    deadline: Optional[date] = Field(None, description='Expiration date of the task')
    status: Optional[str] = Field(None, min_length=1, max_length=21, description='Status of the task')


class STaskUpd(BaseModel):
    id: int = Field(..., ge=1, description='Id of the task to be updated')
    name: Optional[str] = Field(None, min_length=2, max_length=50, description='New name of the task')
    parent_task: Optional[int] = Field(None, ge=1, description='ID of a new parent task')
    employee_id: Optional[int] = Field(None, ge=1, description='ID of a new assignee')
    deadline: Optional[date] = Field(None, description='New expiration date of the task')
    status: Optional[str] = Field(None, min_length=1, max_length=21, description='New status of the task')
