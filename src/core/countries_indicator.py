import logging

from .utils import __get_data, _validate_filter
from .exceptions import BadFilterException, SortByException
from settings import LOGGER_NAME


logger = logging.getLogger(LOGGER_NAME)


def get_countries_filtered_by_indicator(**kwargs):
    """
    Return df filtered by indicator and value given
    """
    df = __get_data()

    indicator = kwargs.get("indicator")
    value = kwargs.get("value")

    if _validate_filter(df["Indicator"].str.lower().values, indicator.lower()):
        df = df[(df["Indicator"].str.lower() == indicator.lower()) &
                (df["Inequality"] == 'Total') &
                (df["Value"] > value)
                ]

        return df, indicator, value
    raise BadFilterException(f"Indicator '{indicator}' not found in data")


async def get_countries(filters_params: dict = {},
                        query_params: dict = {}):
    """
    Return countries applying filters and ordering given
    """

    logger.info(f"get_countries with {filters_params}")

    df, indicator, value = get_countries_filtered_by_indicator(**filters_params)

    logger.info(f"countries len {len(df)}")

    limit = query_params.get("limit")
    skip = query_params.get("skip")
    sort_by, sort_order = query_params.get("sort_by"), query_params.get("sort_order")

    if sort_by is not None:
        # Sort countries
        try:
            df = df.sort_values(sort_by, ascending=(sort_order == 'asc'))
        except KeyError as ex:
            logger.info(f"Can't SortBy {sort_by}")
            logger.error(ex)

            raise SortByException(f"Can't sort results by '{sort_by}', not found in data.")

    # limit results
    total_results = len(df)
    if limit is not None:
        df = df.iloc[skip:skip + limit]

    # use dict as Schema CountryIndicator (schemas.countries_schema.py)
    countries = [{'country': c, 'value': v}
                 for c, v in zip(df['Country'].values, df['Value'].values)]
    return {
        'countries': countries,
        'indicator': indicator,
        'min_value': value,
        'amount_results': len(countries),
        'total_results': total_results
    }
