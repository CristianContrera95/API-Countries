from copy import copy
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_api_working():
    response = client.get("/")
    assert response.status_code == 200

    assert response.json() == {"server": "API Working"}


def test_response_format_keys():
    response = client.get("/countries/")
    assert response.status_code == 200

    response = response.json()
    assert "countries" in list(response.keys())
    assert "indicator" in list(response.keys())
    assert "min_value" in list(response.keys())


def test_response_format_values_types():
    response = client.get("/countries/")
    assert response.status_code == 200

    response = response.json()
    assert isinstance(response["countries"], list)
    assert isinstance(response["indicator"], str)
    assert isinstance(response["min_value"], float) or \
           isinstance(response["min_value"], int)


def test_response_format_countries():
    response = client.get("/countries/")
    assert response.status_code == 200

    countries = response.json()["countries"]

    assert all({isinstance(data, dict) for data in countries})


def test_response_countries_country_not_none():
    response = client.get("/countries/")
    assert response.status_code == 200

    countries = response.json()["countries"]

    assert all({data['country'] is not None for data in countries})


def test_response_countries_value_not_none():
    response = client.get("/countries/")
    assert response.status_code == 200

    countries = response.json()["countries"]

    assert all({data['value'] is not None for data in countries})


def test_skip_limit():
    response = client.get("/countries/",
                          params={
                              'skip': 0,
                              'limit': 10
                          })
    assert response.status_code == 200

    countries = response.json()["countries"]

    assert len(countries) == 10


def test_amount_results():
    response = client.get("/countries/",
                          params={
                              'limit': 10
                          })
    assert response.status_code == 200

    amount_results = response.json()["amount_results"]

    assert amount_results == 10


def test_amount_results_all():
    response = client.get("/countries/",)
    assert response.status_code == 200

    response = response.json()
    amount_results = response["amount_results"]
    total_results = response["total_results"]

    assert amount_results == total_results


def test_skip_limit_bad_range():
    response = client.get("/countries/",
                          params={
                              'skip': 0,
                              'limit': -10
                          })
    assert response.status_code == 400


def test_skip_limit_bad_range_v2():
    response = client.get("/countries/",
                          params={
                              'skip': -10,
                              'limit': -10
                          })
    assert response.status_code == 400


def test_sort_by_asc():
    """
    Test order is right
    """
    response = client.get("/countries/",
                          params={
                              'sort': 'Value:asc',
                          })
    assert response.status_code == 200
    countries = response.json()["countries"]
    # sort return list in asc order
    sorted_countries = sorted(copy(countries), key=lambda x: x['value'])

    assert all([country1['country'] == country2['country'] and
                country1['value'] == country2['value']
                for country1, country2 in zip(countries, sorted_countries)
                ])


def test_sort_by_desc():
    """
    Test order is right
    """
    response = client.get("/countries/",
                          params={
                              'sort': 'Value:desc',
                          })
    assert response.status_code == 200
    countries = response.json()["countries"]
    # sort return list in desc order
    sorted_countries = sorted(copy(countries), key=lambda x: x['value'], reverse=True)

    assert all([country1['country'] == country2['country'] and
                country1['value'] == country2['value']
                for country1, country2 in zip(countries, sorted_countries)
                ])


def test_sort_by_bad_order():
    response = client.get("/countries/",
                          params={
                              'sort': 'Value:xxx',
                          })
    assert response.status_code == 400


def test_sort_by_bad_by():
    response = client.get("/countries/",
                          params={
                              'sort': 'Xxxx:asc',
                          })
    assert response.status_code == 400


def test_countries_consistency():
    """Test countries given are the same on each request"""
    response = client.get("/countries/",
                          params={
                              'skip': 10,
                              'limito': 20,
                              'sort': 'Value:asc',
                          })
    assert response.status_code == 200

    countries1 = response.json()["countries"]

    response = client.get("/countries/",
                          params={
                              'skip': 10,
                              'limito': 20,
                              'sort': 'Value:asc',
                          })
    assert response.status_code == 200

    countries2 = response.json()["countries"]

    assert all([country1['country'] == country2['country'] and
                country1['value'] == country2['value']
                    for country1, country2 in zip(countries1, countries2)
                ])
