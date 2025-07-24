# routers/requests_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from ..models import Request
from ..schemas import RequestCreate, Request
from ..dependencies import get_db_session, role_dependency

requests_router = APIRouter(prefix="/requests", tags=["requests"])

@requests_router.post("/", response_model=Request)
async def create_request(req: RequestCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["create_request"]))):
    db_req = Request(**req.dict())
    db.add(db_req)
    await db.commit()
    await db.refresh(db_req)
    return db_req

@requests_router.get("/", response_model=List[Request])
async def get_requests(db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["view_request"]))):
    result = await db.execute(select(Request))
    return result.scalars().all()

@requests_router.put("/{request_id}", response_model=Request)
async def update_request(request_id: int, req_update: RequestCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["update_request"]))):
    db_req = await db.get(Request, request_id)
    if not db_req:
        raise HTTPException(404, "Request not found")
    update_data = req_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_req, key, value)
    await db.commit()
    await db.refresh(db_req)
    return db_req

@requests_router.post("/approve/{request_id}", response_model=Request)
async def approve_request(request_id: int, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["approve_request"]))):
    db_req = await db.get(Request, request_id)
    if not db_req:
        raise HTTPException(404, "Request not found")
    db_req.status = "approved"
    db_req.approved_by = user.id
    await db.commit()
    await db.refresh(db_req)
    return db_req

@requests_router.delete("/{request_id}")
async def delete_request(request_id: int, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["delete_request"]))):
    db_req = await db.get(Request, request_id)
    if not db_req:
        raise HTTPException(404, "Request not found")
    await db.delete(db_req)
    await db.commit()
    return {"msg": "Request deleted"}