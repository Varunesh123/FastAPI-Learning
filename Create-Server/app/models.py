from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Custodian(Base):
    __tablename__ = "custodians"  # Table name (lowercase for SQLite)

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    owner = Column(String(255))
    email = Column(String(255))
    description = Column(Text(4000))
    active = Column(Boolean)
    inactive_by = Column(String(255))
    inactive_on = Column(DateTime)
    created_by = Column(String(255), nullable=False)
    created_on = Column(DateTime, server_default=func.now(), nullable=False)
    updated_by = Column(String(255))
    updated_on = Column(DateTime)

    # Relationship: One-to-many with CustodianEnvironment
    environments = relationship("CustodianEnvironment", back_populates="custodian")

class Environment(Base):
    __tablename__ = "environments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    promotion_order = Column(Integer)
    governance_email = Column(String(255))
    created_by = Column(String(255), nullable=False)
    created_on = Column(DateTime, server_default=func.now(), nullable=False)
    updated_by = Column(String(255))
    updated_on = Column(DateTime)

    # Relationship: One-to-many with CustodianEnvironment
    custodian_environments = relationship("CustodianEnvironment", back_populates="environment")

class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text(4000))
    created_by = Column(String(255), nullable=False)
    created_on = Column(DateTime, server_default=func.now(), nullable=False)
    updated_by = Column(String(255))
    updated_on = Column(DateTime)

    # Relationship: One-to-many with CustodianEnvironment
    custodian_environments = relationship("CustodianEnvironment", back_populates="platform")

class Region(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text(4000))
    created_by = Column(String(255), nullable=False)
    created_on = Column(DateTime, server_default=func.now(), nullable=False)
    updated_by = Column(String(255))
    updated_on = Column(DateTime)

    # Relationship: One-to-many with CustodianEnvironment (optional)
    custodian_environments = relationship("CustodianEnvironment", back_populates="region")

class CustodianEnvironment(Base):
    __tablename__ = "custodian_environments"

    id = Column(Integer, primary_key=True, index=True)
    custodian_id = Column(Integer, ForeignKey("custodians.id"), nullable=False)
    platform_id = Column(Integer, ForeignKey("platforms.id"), nullable=False)
    environment_id = Column(Integer, ForeignKey("environments.id"), nullable=False)
    region_id = Column(Integer, ForeignKey("regions.id"))
    default_for_region = Column(Boolean)
    key_vault_name = Column(String(63))
    catalog_name = Column(String(255))
    container = Column(String(25))
    created_by = Column(String(255), nullable=False)
    created_on = Column(DateTime, server_default=func.now(), nullable=False)
    updated_by = Column(String(255))
    updated_on = Column(DateTime)

    # Relationships
    custodian = relationship("Custodian", back_populates="environments")
    platform = relationship("Platform", back_populates="custodian_environments")
    environment = relationship("Environment", back_populates="custodian_environments")
    region = relationship("Region", back_populates="custodian_environments")