# Introduction 
This package simplifies fetching and transforming data from the Google Analytics Data GA4 API. The GA4 API returns data in a Google object, which can be a hassle to parse and transform. Using this package, you can create a dictionary with your Google Analytics Property ID, as well as the desired Dimensions, Metrics, Order Bys, and Date Ranges you would like to query. By running the function `run_report_return_json(...)` in `google_analytics_data_json.py`, you can call the GA4 API and retrieve data in JSON format. Using the [Google GA4 Query Explorer](https://ga-dev-tools.web.app/ga4/query-explorer/), you can find all possible Metrics, Dimensions, Order Bys, and Date Ranges.

# Installation
`pip install google-analytics-data-json`

# Getting Started

## Environment Variables
1. After installing the package in your virtual environment, add the `credentials.json` file to your project.
2. Optional: Set an environment variable named `GOOGLE_APPLICATION_CREDENTIALS` equal to the path of the previously mentioned `credentials.json` file.
3. Optional: Set the `GOOGLE_ANALYTICS_PROPERTY_ID` environment variable (required for unit tests).



## Running The Project and Examples
The simpelest way to run the project is to import the function `run_report_return_json(...)` from the file `google_analytics_data_json`. This function takes one parameter called an `analytics_dictionary`, which is used to fetch data from the API and return it in JSON format. The structure of the analytics dictionary should look like:

```python

from google_analytics_data_json.google_analytics_data_json import run_report_return_json

analytics_dictionary = {
    "property_id": "<your property_id>",
    "dimension_names": ["date", "country", "deviceCategory"],
    "metric_names": ["totalUsers", "newUsers"], 
    "order_by_names": [
        {
            "type": "dimension", 
            "value": "date", 
            "descending": False
        },
        {
            "type": "dimension",
            "value": "country", 
            "descending": True
        },
        {
            "type": "metric",
            "value": "newUsers", 
            "descending": True
        }
    ],
    "date_range_values": [
        {
            "start_date": "2022-07-01",
            "end_date": "2022-07-04"
        }
    ]
}

# uses GOOGLE_APPLICATION_CREDENTIALS environment variable path
ga_data: List[dict] = run_report_return_json(analytics_dictionary)

# uses credentials in dict, from a secret manager or similar
from google.oauth2 import service_account
service_account_credentials = service_account.Credentials.from_service_account_info(ga_credentials_secret_dict)
ga_data: List[dict] = run_report_return_json(analytics_dictionary, service_account_credentials=service_account_credentials)

```

It is worth noting that the `dimension_names`, `metric_names`, `order_by_names`, and `date_range_values` are list objects, with the `order_by_names` and `date_range_values` requiring nested dictionaries as shown above. 

Although multiple date ranges can be used, the results from the API can be confusing if the dimension `date` is used - therefore, I suggest only using one date range dictionary if you plan querying the `date` dimension.

If you would like to take advantage of only the API call or only the data transformation, you can import the classes `Ga4Request` from `create_ga4_request.py` or `TransformGa4Data` from `transform_ga4_data.py`. This allows you to control the exact methods which are called in each class, although in most cases you will use all of them.

# Build and Test
The build and tests for the project are hosted [in the project repository](https://github.com/DanielJerrehian/google_analytics_data_json).

Use `python -m unittest` to run the unit tests. A coverage report can also be generated using `coverage run -m unittest` and then running `coverage html`.

The following environment variables should be set for unit tests:
* `GOOGLE_APPLICATION_CREDENTIALS`
* `GOOGLE_ANALYTICS_PROPERTY_ID`
