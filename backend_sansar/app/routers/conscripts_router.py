# routers/conscripts_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from ..models import Conscript
from ..schemas import ConscriptCreate, Conscript
from ..dependencies import get_db_session, role_dependency

conscripts_router = APIRouter(prefix="/conscripts", tags=["conscripts"])

@conscripts_router.post("/", response_model=Conscript)
async def create_conscript(conscript: ConscriptCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["create_conscript"]))):
    db_conscript = Conscript(**conscript.dict())
    db.add(db_conscript)
    await db.commit()
    await db.refresh(db_conscript)
    return db_conscript

@conscripts_router.get("/", response_model=List[Conscript])
async def get_conscripts(db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["view_conscript"]))):
    result = await db.execute(select(Conscript))
    return result.scalars().all()

@conscripts_router.put("/{iin}", response_model=Conscript)
async def update_conscript(iin: str, conscript_update: ConscriptCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["update_conscript"]))):
    db_conscript = await db.get(Conscript, iin)
    if not db_conscript:
        raise HTTPException(404, "Conscript not found")
    update_data = conscript_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_conscript, key, value)
    await db.commit()
    await db.refresh(db_conscript)
    return db_conscript

@conscripts_router.delete("/{iin}")
async def delete_conscript(iin: str, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["delete_conscript"]))):
    db_conscript = await db.get(Conscript, iin)
    if not db_conscript:
        raise HTTPException(404, "Conscript not found")
    await db.delete(db_conscript)
    await db.commit()
    return {"msg": "Conscript deleted"}