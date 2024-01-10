from models.avaaz import Entry
from typing_extensions import Any


def get_by_id(id: str) -> dict[str, Any] | None:
    entry = Entry.query.session.get(Entry, id)
    return entry.to_dict() if entry else None
