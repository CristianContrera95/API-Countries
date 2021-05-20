from fastapi import APIRouter, Depends

from .common import CommonQueryParams, FilterParams
from schemas import CountryIndicatorResponse
from core import get_countries


router = APIRouter()


@router.get("/", response_model=CountryIndicatorResponse)
async def get_countries_list(filter: FilterParams = Depends(FilterParams),
                             query: CommonQueryParams = Depends(CommonQueryParams)):
    """
    Return list of countries applying filter and query
    """
    return await get_countries(filters_params=filter.__dict__,
                               query_params=query.__dict__)
