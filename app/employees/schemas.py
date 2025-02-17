from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class SEmployee(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    first_name: str = Field(..., description='First name of the employee')
    last_name: str = Field(..., description='Last name of the employee')
    job: Optional[str] = Field(None, description='Job of the employee')
    created_at: datetime = Field(..., description='Timestamp of the creation')
    updated_at: datetime = Field(..., description='Timestamp of last update')


class SEmployeeAdd(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=12, description='First name of the employee')
    last_name: str = Field(..., min_length=2, max_length=18, description='Last name of the employee')
    job: Optional[str] = Field(None, description='Job of the employee')


class SEmployeeUpd(BaseModel):
    id: int = Field(..., ge=1, description='Id of the employee to be updated')
    first_name: str = Field(..., min_length=2, max_length=12, description='New first name of the employee')
    last_name: str = Field(..., min_length=2, max_length=18, description='New last name of the employee')
    job: Optional[str] = Field(None, description='New job of the employee')
