from pydantic import BaseModel


class JSONEntry(BaseModel):
    title: str | None
    uri: str | None
    date: str  # PS. I had to use string because Pydantic does not accept date or datetime for the values of JSON.


class BulkRequestBody(BaseModel):
    items: list[JSONEntry]


class BulkResponseBody(BaseModel):
    ok: bool
    error: str | None = None
    length: int | None = None
