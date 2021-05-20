# Aivo API
*********************

This API-REST is very useful to get info about countries and economy indicators as "life satisfaction".

---
## Quickstart

### Set up

Setup **aivo-api** is done in the usual ways. The simplest way is with bash:

Clone repo from GitHub:
``` bash
git clone https://github.com/CristianContrera95/API-Countries.git
cd API-Countries 
```

Set permission to scripts:
``` bash
chmod +x scripts/**
```

Now you can use **virtualenv** or **docker** as next lines:

> - **Virtualenv**:
``` bash
 ./scripts/create_env.sh
./scripts/run.sh
```

> - **docker**:
``` bash
./scripts/build_docker.sh
./scripts/run.sh docker
```
  
Any way **AIVO-api** will be running on [http://localhost:8000]( http://localhost:8000 ),
after this you can receive a list of countries, from the api, using the following endpoints.  

---

## API - EndPoints

This part of the documentation covers all the interfaces of **aivo-api**  

### Countries - `http://<host:port>/countries/`

This endpoint allows you, receive a list of countries filtered using an indicator and value for it.

##### Parameters
These parameters are allowed to filter data

```
# Example url
http://localhost:8000/countries/?indicator=Life+satisfaction&value=2.4&skip=10&limit=10&sort=Value:desc
```

``` python
# Example python
import requests

r = requests.get("http://localhost:8000/countries/",
                 params={"indicator": "Life satisfaction",  # optional
                         "value": 2.4,  
                         "skip": 10,           # optional
                         "limit" :10,          # optional
                         "sort": "Value:desc"  # optional
                         }
                 )
print(r.json())
```

- **indicator**: string   
    Default value : Life satisfaction  
    Indicator to use for filter data  
- **value**: integer  
    Default value : 0  
    Value to use for filter *Indicator*  
- **skip**: integer  
    Default value : 0  
- **limit**: integer  
    Default value : 0  
- **sort**: string  
    Par "column:(asc|desc)" to sort results (ie: ```sort=Value:desc```)
  

##### Response

```
# Example
{
  "countries": [
    {
      "country": "string",
      "value": 0
    }
  ],
  "indicator": "string",
  "min_value": 0,
  "amount_results": 0,
  "total_results": 0
}
```

- **countries**: List\[dict(country: string, value: int)]  
    List of countries with their values  
- **indicator**: string  
    Parameter indicator given  
-  **min_value**: integer  
    Parameter value given  
-  **amount_results**: integer  
    amount results given   
-  **total_results**: integer  
    total results without using skip and limit  


> - Note:
  If and error occurs the response will be:
``` 
# Example
{
    "detail": "Error message"
}
```