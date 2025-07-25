# routers/devices_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
import ping3
from ..models import Device
from ..schemas import DeviceCreate, Device
from ..dependencies import get_db_session, role_dependency

devices_router = APIRouter(prefix="/devices", tags=["devices"])

@devices_router.post("/", response_model=Device)
async def create_device(device: DeviceCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    db_device = Device(**device.dict())
    db.add(db_device)
    await db.commit()
    await db.refresh(db_device)
    return db_device

@devices_router.get("/", response_model=List[Device])
async def get_devices(db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["view_devices"]))):
    result = await db.execute(select(Device))
    return result.scalars().all()

@devices_router.get("/status/{device_id}")
async def get_device_status(device_id: int, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["view_status"]))):
    db_device = await db.get(Device, device_id)
    if not db_device:
        raise HTTPException(404, "Device not found")
    status = "up" if ping3.ping(db_device.ip_address) else "down"
    return {"id": device_id, "status": status}

@devices_router.put("/{device_id}", response_model=Device)
async def update_device(device_id: int, device_update: DeviceCreate, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    db_device = await db.get(Device, device_id)
    if not db_device:
        raise HTTPException(404, "Device not found")
    update_data = device_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_device, key, value)
    await db.commit()
    await db.refresh(db_device)
    return db_device

@devices_router.delete("/{device_id}")
async def delete_device(device_id: int, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["admin"]))):
    db_device = await db.get(Device, device_id)
    if not db_device:
        raise HTTPException(404, "Device not found")
    await db.delete(db_device)
    await db.commit()
    return {"msg": "Device deleted"}