from sqlalchemy.orm import relationship, declarative_base, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, Table
from ..database import Base
from typing import List, Optional, TYPE_CHECKING


class UrlsPair(Base):
    __tablename__ = 'short_urls'
    slug: Mapped[str] = mapped_column(primary_key=True, index=True, unique=True)
    long_url: Mapped[str] = mapped_column(index=True)