from datetime import datetime

from models.base import db
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Entry(db.Model):
    __tablename__ = "entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=True)
    uri: Mapped[str] = mapped_column(String(255), nullable=True)
    date: Mapped[datetime] = mapped_column(db.DateTime, nullable=False)

    def to_dict(self) -> dict[str, str]:
        return {
            "title": str(self.title),
            "uri": str(self.uri),
            "date": str(self.date),
        }
