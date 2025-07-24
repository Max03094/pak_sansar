# schemas.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class RoleBase(BaseModel):
    name: str
    permissions: dict

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int

class MilitaryOfficeBase(BaseModel):
    district: Optional[str]
    city: Optional[str]
    name: str
    chief_phone: Optional[str]

class MilitaryOfficeCreate(MilitaryOfficeBase):
    pass

class MilitaryOffice(MilitaryOfficeBase):
    id: int

class UserBase(BaseModel):
    full_name: str
    role_id: int
    ip_address: Optional[str]
    mac_address: Optional[str]
    military_office_id: Optional[int]
    phone_number: Optional[str]

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

class AlertBase(BaseModel):
    priority: int
    type: Optional[str]
    description: Optional[str]
    military_office_id: int

class AlertCreate(AlertBase):
    pass

class Alert(AlertBase):
    id: int
    created_at: datetime

class AlertStatusBase(BaseModel):
    alert_id: int
    user_id: int
    received_at: Optional[datetime]
    accepted_at: Optional[datetime]
    ready_at: Optional[datetime]

class AlertStatusCreate(AlertStatusBase):
    pass

class AlertStatus(AlertStatusBase):
    id: int
    total_time: Optional[str]

class EventsPSBase(BaseModel):
    type: Optional[str]
    source: Optional[str]
    military_office_id: int
    status: Optional[str]

class EventsPSCreate(EventsPSBase):
    pass

class EventsPS(EventsPSBase):
    id: int
    timestamp: datetime

class EmployeeBase(BaseModel):
    full_name: str
    rank: Optional[str]
    position: Optional[str]
    phone_number: Optional[str]
    telegram_id: Optional[str]
    military_office_id: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

class ConscriptBase(BaseModel):
    iin: str
    full_name: str
    photo_url: Optional[str]
    status: Optional[str]
    comment: Optional[str]

class ConscriptCreate(ConscriptBase):
    pass

class Conscript(ConscriptBase):
    added_at: datetime

class RequestBase(BaseModel):
    conscript_iin: str
    type: Optional[str]
    comment: Optional[str]
    approved_by: Optional[int]
    escort_id: Optional[int]
    status: Optional[str]

class RequestCreate(RequestBase):
    pass

class Request(RequestBase):
    id: int
    created_at: datetime

class DeviceBase(BaseModel):
    type: Optional[str]
    ip_address: Optional[str]
    login: Optional[str]
    password: Optional[str]
    military_office_id: int
    status: Optional[str]

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int