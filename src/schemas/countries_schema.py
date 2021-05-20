from typing import List
from pydantic import BaseModel


class CountryIndicator(BaseModel):
    country: str
    value: float


class CountryIndicatorResponse(BaseModel):
    countries: List[CountryIndicator]
    indicator: str
    min_value: int
    amount_results: int
    total_results: int
