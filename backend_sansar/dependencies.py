# dependencies.py
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from .models import User
from fastapi_users import FastAPIUsers
from .auth import backend

async def get_db_session() -> AsyncSession:
    async with async_session() as session:
        yield session

def role_dependency(required_permissions: List[str]):
    async def check_role(user: User = Depends(fastapi_users.current_user(active=True))):
        if not user.role or not all(perm in user.role.permissions for perm in required_permissions):
            raise HTTPException(403, "Insufficient permissions")
        return user
    return check_role