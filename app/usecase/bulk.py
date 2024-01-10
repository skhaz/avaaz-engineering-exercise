import traceback

from dateutil import parser
from dto.avaaz import JSONEntry
from models.avaaz import Entry
from models.base import db


def bulk_insert(items: list[JSONEntry]):
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
                items,
            )
        )

        db.session.commit()
    except Exception as exc:
        traceback.print_exception(exc)
        db.session.rollback()
        raise exc
