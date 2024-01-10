from datetime import datetime
from typing import Any

from models.base import db
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Entry(db.Model):
    __tablename__ = "entries"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=True, index=True)
    uri: Mapped[str] = mapped_column(String(255), nullable=True, index=True)
    date: Mapped[datetime] = mapped_column(db.DateTime, nullable=False, index=True)

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "uri": self.uri,
            "date": self.date,
        }
