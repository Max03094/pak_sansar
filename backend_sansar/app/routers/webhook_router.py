# routers/webhook_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import Request, AlertStatus
from ..dependencies import get_db_session
from ..websocket import manager

webhook_router = APIRouter(prefix="/webhooks", tags=["webhooks"])

@webhook_router.post("/skud/event")
async def skud_event(event: dict, db: AsyncSession = Depends(get_db_session)):
    if "entry" in event.get("type", ""):
        req = await db.execute(select(Request).where(Request.conscript_iin == event.get("iin"), Request.status == "approved"))
        db_req = req.scalar_one_or_none()
        if db_req:
            db_req.status = "entered"
            await db.commit()
            await manager.broadcast({"type": "request_update", "data": db_req.id}, db_req.approved_by)
    elif "exit" in event.get("type", ""):
        # Similar update to exited
        pass
    return {"msg": "Event processed"}