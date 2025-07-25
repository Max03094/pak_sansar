# routers/military_offices_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from ..models import MilitaryOffice
from ..schemas import MilitaryOfficeCreate, MilitaryOffice
from ..dependencies import get_db_session, role_dependency

military_offices_router = APIRouter(prefix="/military-offices", tags=["military_offices"])

@military_offices_router.post("/", response_model=MilitaryOffice)
async def create_office(office: MilitaryOfficeCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    db_office = MilitaryOffice(**office.dict())
    db.add(db_office)
    await db.commit()
    await db.refresh(db_office)
    return db_office

@military_offices_router.get("/", response_model=List[MilitaryOffice])
async def get_offices(db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["view_offices"]))):
    result = await db.execute(select(MilitaryOffice))
    return result.scalars().all()

@military_offices_router.put("/{office_id}", response_model=MilitaryOffice)
async def update_office(office_id: int, office_update: MilitaryOfficeCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    db_office = await db.get(MilitaryOffice, office_id)
    if not db_office:
        raise HTTPException(404, "Office not found")
    update_data = office_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_office, key, value)
    await db.commit()
    await db.refresh(db_office)
    return db_office

@military_offices_router.delete("/{office_id}")
async def delete_office(office_id: int, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    db_office = await db.get(MilitaryOffice, office_id)
    if not db_office:
        raise HTTPException(404, "Office not found")
    await db.delete(db_office)
    await db.commit()
    return {"msg": "Office deleted"}