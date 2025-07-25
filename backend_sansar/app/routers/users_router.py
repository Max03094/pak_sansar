# routers/users_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from ..models import User
from ..schemas import UserCreate, User, UserUpdate
from ..dependencies import get_db_session, role_dependency

users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.post("/", response_model=User)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db_session), current_user = Depends(role_dependency(["admin"]))):
    db_user = User(**user.dict(exclude={"password"}))  # Handle password hashing via fastapi-users
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

@users_router.get("/", response_model=List[User])
async def get_users(db: AsyncSession = Depends(get_db_session), current_user = Depends(role_dependency(["view_users"]))):
    result = await db.execute(select(User))
    return result.scalars().all()

@users_router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserUpdate, db: AsyncSession = Depends(get_db_session), current_user = Depends(role_dependency(["admin"]))):
    db_user = await db.get(User, user_id)
    if not db_user:
        raise HTTPException(404, "User not found")
    update_data = user_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    await db.commit()
    await db.refresh(db_user)
    return db_user

@users_router.delete("/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db_session), current_user = Depends(role_dependency(["admin"]))):
    db_user = await db.get(User, user_id)
    if not db_user:
        raise HTTPException(404, "User not found")
    await db.delete(db_user)
    await db.commit()
    return {"msg": "User deleted"}