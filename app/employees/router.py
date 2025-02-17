from typing import Union

from fastapi import APIRouter, Depends

from app.employees.request_body import RBEmployee
from app.employees.dao import EmployeeDAO
from app.employees.schemas import SEmployee, SEmployeeAdd, SEmployeeUpd


router = APIRouter(prefix='/employees', tags=['Work with employees'])


@router.get('', summary='Get all employees')
async def get_all_employees(request_body: RBEmployee = Depends()) -> list[SEmployee]:
    return await EmployeeDAO.find_all(**request_body.to_dict())


@router.get('/{employee_id}', summary='Get one employee or none by id')
async def get_one_or_none_employee_by_id(employee_id: int) -> Union[SEmployee, dict]:
    result = await EmployeeDAO.find_one_or_none(id=employee_id)
    return result if result is not None else {'message': f'Employee with id \'{employee_id}\' is not found!'}


@router.post('/add', summary='Add new employee in database')
async def add_employee(employee: SEmployeeAdd) -> dict:
    new_employee = await EmployeeDAO.add(**employee.model_dump())
    if new_employee:
        return {'message': 'Employee is added successfully!', 'employee': new_employee.to_dict()}
    else:
        print('Good2')
        return {'message': 'Error while adding new employee!'}


@router.put('/update-one', summary='Update an employee by id')
async def update_employee(employee: SEmployeeUpd) -> dict:
    affected_rows = await EmployeeDAO.update(filter_by={'id': employee.id}, **employee.model_dump(exclude={'id'}))
    if affected_rows:
        return {'message': f'Employee with id \'{employee.id}\' is updated successfully!', 'employee': employee}
    else:
        return {'message': f'Error while updating employee with id \'{employee.id}\'!'}


@router.delete("/delete/{employee_id}")
async def delete_employee(employee_id: int) -> dict:
    affected_rows = await EmployeeDAO.delete(id=employee_id)
    if affected_rows:
        return {'message': f'Employee with id \'{employee_id}\' is deleted!'}
    else:
        return {'message': f'Error while deleting employee with id \'{employee_id}\'!'}
