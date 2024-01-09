import traceback

from dateutil import parser
from dto.bulk import BulkRequestBody
from dto.bulk import BulkResponseBody
from flask import Blueprint
from flask_pydantic import validate
from models.avaaz import Entry
from models.base import db

blueprint = Blueprint("avaaz", __name__)


@blueprint.get("/")
def index():
    return {"ok3": Entry.query.first().to_dict()}


@blueprint.post("/bulk")
@validate()
def bulk(body: BulkRequestBody) -> BulkResponseBody:
    try:
        db.session.add_all(
            map(
                lambda i: Entry(  # type: ignore # Pyright gets confused with SQLAlchemy's metaclasses.
                    title=i.title,
                    uri=i.uri,
                    date=parser.parse(
                        i.date
                    ),  # NOTE: I'm not sure if all the dates are being correctly parsed, this would be for a second stage of improvement and bug fixing.
                ),
                body.items,
            )
        )

        db.session.commit()
    except Exception as exc:
        traceback.print_exception(exc)
        db.session.rollback()
        return BulkResponseBody(ok=False, error=str(exc))

    return BulkResponseBody(ok=True, length=len(body.items))
