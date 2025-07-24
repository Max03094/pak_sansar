# routers/skud_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import Device, Conscript
from ..dependencies import get_db_session, role_dependency
from ..integrations.dahua import add_face

skud_router = APIRouter(prefix="/skud", tags=["skud"])

@skud_router.post("/add-face")
async def add_face_to_skud(conscript_iin: str, photo_base64: str, db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["add_face"]))):
    conscript = await db.get(Conscript, conscript_iin)
    if not conscript:
        raise HTTPException(404, "Conscript not found")
    result = await db.execute(select(Device).where(Device.type == "skud", Device.military_office_id == user.military_office_id))
    device = result.scalar_one_or_none()
    if not device:
        raise HTTPException(404, "SKUD device not found")
    result = add_face(device.ip_address, device.login, device.password, photo_base64, conscript_iin)
    if "error" in result:
        raise HTTPException(500, "Failed to add face")
    return {"msg": "Face added successfully"}