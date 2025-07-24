# routers/events_ps_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from ..models import EventsPS
from ..schemas import EventsPSCreate, EventsPS
from ..dependencies import get_db_session, role_dependency

events_ps_router = APIRouter(prefix="/events-ps", tags=["events_ps"])

@events_ps_router.post("/", response_model=EventsPS)
async def create_event(event: EventsPSCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["create_event"]))):
    db_event = EventsPS(**event.dict())
    db.add(db_event)
    await db.commit()
    await db.refresh(db_event)
    return db_event

@events_ps_router.get("/", response_model=List[EventsPS])
async def get_events(db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["view_events"]))):
    result = await db.execute(select(EventsPS))
    return result.scalars().all()

@events_ps_router.put("/{event_id}", response_model=EventsPS)
async def update_event(event_id: int, event_update: EventsPSCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["update_event"]))):
    db_event = await db.get(EventsPS, event_id)
    if not db_event:
        raise HTTPException(404, "Event not found")
    update_data = event_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_event, key, value)
    await db.commit()
    await db.refresh(db_event)
    return db_event

@events_ps_router.delete("/{event_id}")
async def delete_event(event_id: int, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["delete_event"]))):
    db_event = await db.get(EventsPS, event_id)
    if not db_event:
        raise HTTPException(404, "Event not found")
    await db.delete(db_event)
    await db.commit()
    return {"msg": "Event deleted"}