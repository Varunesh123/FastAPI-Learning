from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Custodian Schemas
class CustodianBase(BaseModel):
    name: str
    owner: Optional[str] = None
    email: Optional[str] = None
    description: Optional[str] = None
    active: Optional[bool] = None
    inactive_by: Optional[str] = None
    inactive_on: Optional[datetime] = None
    created_by: str

class CustodianCreate(CustodianBase):
    pass

class CustodianUpdate(BaseModel):
    name: Optional[str] = None
    owner: Optional[str] = None
    # ... (add other optional fields as needed)
    updated_by: str

class Custodian(CustodianBase):
    id: int
    created_on: datetime
    updated_on: Optional[datetime] = None

    class Config:
        from_attributes = True  # For SQLAlchemy compatibility

# Environment Schemas (similar pattern; abbreviated)
class EnvironmentBase(BaseModel):
    name: str
    promotion_order: Optional[int] = None
    governance_email: Optional[str] = None
    created_by: str

class EnvironmentCreate(EnvironmentBase):
    pass

class Environment(EnvironmentBase):
    id: int
    created_on: datetime
    updated_on: Optional[datetime] = None

    class Config:
        from_attributes = True

# Platform Schemas (abbreviated)
class PlatformBase(BaseModel):
    name: str
    description: Optional[str] = None
    created_by: str

class PlatformCreate(PlatformBase):
    pass

class Platform(PlatformBase):
    id: int
    created_on: datetime
    updated_on: Optional[datetime] = None

    class Config:
        from_attributes = True

# Region Schemas (abbreviated)
class RegionBase(BaseModel):
    name: str
    description: Optional[str] = None
    created_by: str

class RegionCreate(RegionBase):
    pass

class Region(RegionBase):
    id: int
    created_on: datetime
    updated_on: Optional[datetime] = None

    class Config:
        from_attributes = True

# CustodianEnvironment Schemas (abbreviated)
class CustodianEnvironmentBase(BaseModel):
    custodian_id: int
    platform_id: int
    environment_id: int
    region_id: Optional[int] = None
    default_for_region: Optional[bool] = None
    key_vault_name: Optional[str] = None
    catalog_name: Optional[str] = None
    container: Optional[str] = None
    created_by: str

class CustodianEnvironmentCreate(CustodianEnvironmentBase):
    pass

class CustodianEnvironment(CustodianEnvironmentBase):
    id: int
    created_on: datetime
    updated_on: Optional[datetime] = None

    class Config:
        from_attributes = True