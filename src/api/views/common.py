from enum import Enum
from typing import Optional

from core.exceptions import BadFilterException


SORT_SEPARATOR_CHAR = ":"


class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"


def cast_sort_parameters(raw_parameter):
    """Format Sort param to sort_by and sort_order"""
    if raw_parameter is None:
        return None, None

    if len(raw_parameter.split(SORT_SEPARATOR_CHAR)) != 2:
        raise BadFilterException("Invalid sort parameter")

    tokens = raw_parameter.split(SORT_SEPARATOR_CHAR)
    try:
        return tokens[0], SortOrder(tokens[1])
    except ValueError:
        raise BadFilterException("Invalid sort parameter")


class CommonQueryParams:

    def __init__(self, skip: Optional[int] = 0,
                 limit: Optional[int] = None,
                 sort: Optional[str] = None):
        if skip < 0 or (limit is not None and limit < 0):
            raise BadFilterException(
                "Negative values for skip or limit not allowed"
            )
        self.skip = skip
        self.limit = limit
        self.sort_by, self.sort_order = cast_sort_parameters(sort)


class FilterParams:

    def __init__(self,
                 indicator: Optional[str] = "Life satisfaction",
                 value: Optional[float] = 0,
                 ):
        if value < 0:
            raise BadFilterException(
                "Negative values for 'value' not allowed"
            )
        self.indicator = indicator
        self.value = value
