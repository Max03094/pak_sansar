# routers/video_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import Device
from ..dependencies import get_db_session, role_dependency

video_router = APIRouter(prefix="/video", tags=["video"])

@video_router.get("/stream/{device_id}")
async def get_video_stream(device_id: int, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["view_video"]))):
    db_device = await db.get(Device, device_id)
    if not db_device or db_device.type != "camera":
        raise HTTPException(404, "Camera not found")
    stream_url = f"rtsp://{db_device.login}:{db_device.password}@{db_device.ip_address}:554/cam/realmonitor?channel=1&subtype=0"
    return {"stream_url": stream_url}