from dto.avaaz import BulkRequestBody
from dto.avaaz import BulkResponseBody
from dto.avaaz import NotFoundResponse
from dto.avaaz import SearchQuery
from flask import Blueprint
from flask_pydantic import validate

from app.cache.redis import cache
from app.usecase.bulk import bulk_insert
from app.usecase.get import get_by_id
from app.usecase.search import fuzzy_search

blueprint = Blueprint("avaaz", __name__)


@blueprint.get("/<id>")
@validate()
@cache()
def get(id: str):
    result = get_by_id(id)
    if not result:
        return NotFoundResponse(), 404

    return result


@blueprint.get("/")
@validate()
@cache()
def search(query: SearchQuery):
    result = fuzzy_search(query.after, query.before, query.contains, query.uri)
    if not result:
        return NotFoundResponse(), 404

    return [entry.to_dict() for entry in result]


@blueprint.post("/bulk")
@validate()
def bulk(body: BulkRequestBody) -> tuple[BulkResponseBody, int]:
    try:
        bulk_insert(body.items)
        return BulkResponseBody(ok=True), 200
    except:  # noqa
        pass

    return BulkResponseBody(ok=False), 500
