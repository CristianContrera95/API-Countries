# Aivo API
*********************

This API-REST is very useful to get info about countries and economy indicators as "life satisfaction".

---
## Quickstart

### Set up

Setup **aivo-api** is done in the usual ways. The simplest way is with bash:

Clone repo from GitHub:
``` bash
git clone
cd aivo_challenge 
```

Set permission to scripts
``` bash
chmod +x scripts/**
```

Now you can use virtualenv as next lines:
``` bash
./scripts/create_env.sh
./scripts/run.sh
```

Or use docker:
``` bash
./scripts/build_docker.sh
./scripts/run.sh docker
```

Any way set up **AIVO-api** on http://localhost:8000, after this you can request to api for countries using the follow endpoints
---

## API - EndPoints

This part of the documentation covers all the interfaces of **aivo-api**  

### Countries 
##### http://<host:port\>/countries/

##### Parameters
These parameters are allowed to filter data

```
# Example
http://localhost:5000/countries/?indicator=Life+satisfactionvalue=2.4&skip=10&limit=10&sort=Value:desc
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
    Par "Columns:\<asc|desc>" to sort results  
  

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
  **min_value**: integer  
    Parameter value given  
  **amount_results**: integer  
    amount results given   
  **total_results**: integer  
    total results without using skip and limit  


- Note:
  If and error occurs the response will be:
 
``` 
# Example
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```