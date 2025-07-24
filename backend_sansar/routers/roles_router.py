# routers/roles_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from ..models import Role
from ..schemas import RoleCreate, Role
from ..dependencies import get_db_session, role_dependency

roles_router = APIRouter(prefix="/roles", tags=["roles"])

@roles_router.post("/", response_model=Role)
async def create_role(role: RoleCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    db_role = Role(**role.dict())
    db.add(db_role)
    await db.commit()
    await db.refresh(db_role)
    return db_role

@roles_router.get("/", response_model=List[Role])
async def get_roles(db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    result = await db.execute(select(Role))
    return result.scalars().all()

@roles_router.put("/{role_id}", response_model=Role)
async def update_role(role_id: int, role_update: RoleCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    db_role = await db.get(Role, role_id)
    if not db_role:
        raise HTTPException(404, "Role not found")
    update_data = role_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_role, key, value)
    await db.commit()
    await db.refresh(db_role)
    return db_role

@roles_router.delete("/{role_id}")
async def delete_role(role_id: int, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    db_role = await db.get(Role, role_id)
    if not db_role:
        raise HTTPException(404, "Role not found")
    await db.delete(db_role)
    await db.commit()
    return {"msg": "Role deleted"}