# routers/notifications_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from celery import Celery
from twilio.rest import Client
from telegram import Bot, ParseMode
from ..dependencies import get_db_session
from ..models import Employee, Alert
from ..schemas import Alert

notifications_router = APIRouter(prefix="/notifications", tags=["notifications"])

celery = Celery('sansar', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

# Configure Twilio and Telegram
TWILIO_SID = "your_twilio_sid"
TWILIO_TOKEN = "your_twilio_token"
TWILIO_FROM = "+1234567890"
TELEGRAM_TOKEN = "your_telegram_token"

@celery.task
def send_sms(phone: str, message: str):
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    client.messages.create(to=phone, from_=TWILIO_FROM, body=message)

@celery.task
def send_telegram(telegram_id: str, message: str):
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=telegram_id, text=message, parse_mode=ParseMode.HTML)

@notifications_router.post("/send/{alert_id}")
async def send_notifications(alert_id: int, methods: List[str], db: AsyncSession = Depends(get_db_session)):
    alert = await db.get(Alert, alert_id)
    if not alert:
        raise HTTPException(404, "Alert not found")
    result = await db.execute(select(Employee).where(Employee.military_office_id == alert.military_office_id))
    employees = result.scalars().all()
    template = f"Внимание тревога! [{alert.type}] [{alert.description}]"
    for employee in employees:
        if "sms" in methods and employee.phone_number:
            send_sms.delay(employee.phone_number, template)
        if "telegram" in methods and employee.telegram_id:
            send_telegram.delay(employee.telegram_id, template)
    return {"msg": "Notifications queued"}