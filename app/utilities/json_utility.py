
import datetime
import json


def to_json(obj: any) -> str:
    """
    Converts the given object to a JSON string.

    Returns:
        json (str): The provided obj as a JSON string.
    """

    return json.dumps(obj, default=__convert, indent=4, sort_keys=True)


def __convert(obj: any) -> any:

    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()

    return obj.__dict__
