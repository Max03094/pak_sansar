# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP, JSON, CheckConstraint, Interval, Computed
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
# from datetime import datetime # Эта строка не используется в текущем коде, можно удалить

Base = declarative_base()

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    permissions = Column(JSON)

class MilitaryOffice(Base):
    __tablename__ = "military_offices"
    id = Column(Integer, primary_key=True)
    district = Column(String(100))
    city = Column(String(100))
    name = Column(String(255), nullable=False)
    chief_phone = Column(String(20))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    ip_address = Column(String(45))
    mac_address = Column(String(17))
    military_office_id = Column(Integer, ForeignKey("military_offices.id"))
    phone_number = Column(String(20))
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp()) # Добавлен onupdate
    secret_2fa = Column(String(32))  # For 2FA
    role = relationship("Role")
    military_office = relationship("MilitaryOffice")

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    priority = Column(Integer, CheckConstraint("priority BETWEEN 1 AND 5"))
    type = Column(String(50))
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    military_office_id = Column(Integer, ForeignKey("military_offices.id"))
    military_office = relationship("MilitaryOffice")

class AlertStatus(Base):
    __tablename__ = "alert_statuses"
    id = Column(Integer, primary_key=True)
    alert_id = Column(Integer, ForeignKey("alerts.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id"))
    received_at = Column(TIMESTAMP)
    accepted_at = Column(TIMESTAMP)
    ready_at = Column(TIMESTAMP)
    # Исправлено: использование Computed для создания вычисляемого столбца
    total_time = Column(Interval, Computed("(ready_at - received_at)"))

class EventsPS(Base):
    __tablename__ = "events_ps"
    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    source = Column(String(100))
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp())
    military_office_id = Column(Integer, ForeignKey("military_offices.id"))
    status = Column(String(20))

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(255), nullable=False)
    rank = Column(String(50))
    position = Column(String(100))
    phone_number = Column(String(20))
    telegram_id = Column(String(50))
    military_office_id = Column(Integer, ForeignKey("military_offices.id"))

class Conscript(Base):
    __tablename__ = "conscripts"
    iin = Column(String(12), primary_key=True)
    full_name = Column(String(255), nullable=False)
    photo_url = Column(String(255))
    added_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    status = Column(String(50))
    comment = Column(Text)

class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True)
    conscript_iin = Column(String(12), ForeignKey("conscripts.iin", ondelete="CASCADE"))
    type = Column(String(50))
    comment = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    approved_by = Column(Integer, ForeignKey("users.id"))
    escort_id = Column(Integer, ForeignKey("employees.id"))
    status = Column(String(50))

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    ip_address = Column(String(45))
    login = Column(String(50))
    password = Column(String(100))
    military_office_id = Column(Integer, ForeignKey("military_offices.id"))
    status = Column(String(20))