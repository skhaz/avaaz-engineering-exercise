from datetime import date

from pydantic import BaseModel


class JSONEntry(BaseModel):
    title: str | None
    uri: str | None
    date: str  # PS. I had to use string because Pydantic does not accept date or datetime for the values of JSON.


class BulkRequestBody(BaseModel):
    items: list[JSONEntry]


class BulkResponseBody(BaseModel):
    ok: bool


class SearchQuery(BaseModel):
    after: date | None = None
    before: date | None = None
    contains: str | None = None
    uri: str | None = None


class NotFoundResponse(BaseModel):
    ok: bool = False
    error: str = "Not found"
