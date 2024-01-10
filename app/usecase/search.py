from datetime import date

from models.avaaz import Entry


def fuzzy_search(
    after: date | None,
    before: date | None,
    cotains: str | None,
    uri: str | None,
) -> list[Entry]:
    filter = []

    if after:
        filter.append(Entry.date >= after)

    if before:
        filter.append(Entry.date <= before)

    if cotains:
        filter.append(Entry.title.contains(cotains))

    if uri:
        filter.append(Entry.uri.contains(uri))

    return Entry.query.filter(*filter).all()
