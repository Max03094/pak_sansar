# main.py
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from contextlib import asynccontextmanager
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend
from fastapi_users.db import SQLAlchemyUserDatabase
from .models import User, Base
from .schemas import UserCreate, UserRead, UserUpdate
from .dependencies import get_db_session
from .routers import alerts_router, users_router, roles_router, military_offices_router, notifications_router, events_ps_router, employees_router, conscripts_router, requests_router, devices_router, video_router, skud_router, audio_router, reports_router
from .websocket import websocket_router
from .auth import UserManager, get_user_db, SECRET_KEY, get_jwt_strategy
import pyotp
import logging

logging.basicConfig(level=logging.INFO)

engine = create_async_engine("postgresql+asyncpg://user:pass@localhost/sansar_db", echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

user_db = SQLAlchemyUserDatabase(User, async_session)
backend = AuthenticationBackend(
    name="jwt",
    transport=BearerTransport(tokenUrl="auth/jwt/login"),
    get_strategy=get_jwt_strategy,
)
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [backend],
)
app.include_router(fastapi_users.get_auth_router(backend), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"])

app.include_router(alerts_router)
app.include_router(users_router)
app.include_router(roles_router)
app.include_router(military_offices_router)
app.include_router(notifications_router)
app.include_router(events_ps_router)
app.include_router(employees_router)
app.include_router(conscripts_router)
app.include_router(requests_router)
app.include_router(devices_router)
app.include_router(video_router)
app.include_router(skud_router)
app.include_router(audio_router)
app.include_router(reports_router)
app.include_router(websocket_router)
app.include_router(webhook_router)
app.include_router(ai_router)

@app.post("/auth/2fa-verify")
async def verify_2fa(token: str, user: User = Depends(fastapi_users.current_user())):
    totp = pyotp.TOTP(user.secret_2fa)
    if totp.verify(token):
        return {"msg": "2FA verified"}
    raise HTTPException(401, "Invalid 2FA")