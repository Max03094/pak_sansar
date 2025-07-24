# routers/employees_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from ..models import Employee
from ..schemas import EmployeeCreate, Employee
from ..dependencies import get_db_session, role_dependency

employees_router = APIRouter(prefix="/employees", tags=["employees"])

@employees_router.post("/", response_model=Employee)
async def create_employee(employee: EmployeeCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    await db.commit()
    await db.refresh(db_employee)
    return db_employee

@employees_router.get("/", response_model=List[Employee])
async def get_employees(db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["view_employees"]))):
    result = await db.execute(select(Employee))
    return result.scalars().all()

@employees_router.put("/{employee_id}", response_model=Employee)
async def update_employee(employee_id: int, employee_update: EmployeeCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    db_employee = await db.get(Employee, employee_id)
    if not db_employee:
        raise HTTPException(404, "Employee not found")
    update_data = employee_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_employee, key, value)
    await db.commit()
    await db.refresh(db_employee)
    return db_employee

@employees_router.delete("/{employee_id}")
async def delete_employee(employee_id: int, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    db_employee = await db.get(Employee, employee_id)
    if not db_employee:
        raise HTTPException(404, "Employee not found")
    await db.delete(db_employee)
    await db.commit()
    return {"msg": "Employee deleted"}