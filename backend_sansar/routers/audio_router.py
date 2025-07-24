# routers/audio_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import Device
from ..dependencies import get_db_session, role_dependency
from ..integrations.pi_audio import send_audio

audio_router = APIRouter(prefix="/audio", tags=["audio"])

@audio_router.post("/send")
async def send_audio_notification(office_id: int, mp3_url: str, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["send_audio"]))):
    result = await db.execute(select(Device).where(Device.type == "pi_audio", Device.military_office_id == office_id))
    device = result.scalar_one_or_none()
    if not device:
        raise HTTPException(404, "Audio device not found")
    result = send_audio(device.ip_address, mp3_url)
    if "error" in result:
        raise HTTPException(500, "Failed to send audio")
    return {"msg": "Audio sent"}