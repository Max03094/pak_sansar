# routers/alerts_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from ..models import Alert, AlertStatus
from ..schemas import AlertCreate, Alert, AlertStatusCreate, AlertStatus
from ..dependencies import get_db_session, role_dependency
from ..websocket import manager

alerts_router = APIRouter(prefix="/alerts", tags=["alerts"])

@alerts_router.post("/", response_model=Alert)
async def create_alert(alert: AlertCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["create_alert"]))):
    db_alert = Alert(**alert.dict())
    db.add(db_alert)
    await db.commit()
    await db.refresh(db_alert)
    await manager.broadcast({"type": "new_alert", "data": alert.dict()}, db_alert.military_office_id)  # Broadcast to office
    return db_alert

@alerts_router.get("/", response_model=List[Alert])
async def get_alerts(db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["view_alert"]))):
    result = await db.execute(select(Alert))
    return result.scalars().all()

@alerts_router.put("/status/{alert_id}", response_model=AlertStatus)
async def update_status(alert_id: int, status: AlertStatusCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["update_status"]))):
    db_status = AlertStatus(**status.dict())
    db.add(db_status)
    await db.commit()
    await db.refresh(db_status)
    await manager.broadcast({"type": "status_update", "data": status.dict()}, user.military_office_id)
    return db_status