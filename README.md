# Introduction 
This package can be used to simplify fetching and transforming data from the Google Analytics Data GA4 API. As of the time writing this, the GA4 API returns data in a Google object, which can be a hassle to parse and trasnform. Using this package, you can create a dictionary with your Google Analytics Property ID, as well as the desired Dimensions, Metrics, Order Bys, and Date Ranges you would like to query. By running the function `run_report_return_json` in `google_analytics_data_json.py`, you can call the GA4 API and retrieve data in JSON format. Using this tool provided by Google, you can find all possible Metrics, Dimensions, Order Bys, and Date Ranges that can be used: https://ga-dev-tools.web.app/ga4/query-explorer/

# Installation
`pip install google-analytics-data-json`

# Getting Started
After installing the package in your virtual environment, add the `credentials.json` file to your project. Then, set an environment variable named `GOOGLE_APPLICATION_CREDENTIALS` equal to the path of the previously mentioned `credentials.json` file.

# Running The Project
The simpelest way to run the project is to import the function `run_report_return_json` from the file `google_analytics_data_json`. This function takes one parameter called an `analytics_dictionary`, which is used to fetch data from the API. The structure of the analytics dictionary should be as follows:

```python
{
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
```

It is worth noting that the `dimension_names`, `metric_names`, `order_by_names`, and `date_range_values` are list objects, with the `order_by_names` and `date_range_values` requiring nested dictionaries as shown above. 

Although multiple date ranges can be used, the results from the API can be confusing if the dimension `date` is used - therefore, I suggest only using one date range dictionary if you plan querying the `date` dimension.

If you would like to take advantage of only the API call or only the data transformation, you can import the classes `Ga4Request` from `create_ga4_request.py` or `TransformGa4Data` from `transform_ga4_data.py`. This allows you to control the exact methods which are called in each class, although in most cases you will use all of them.

# Build and Test
python -m unittest is used to run the tests. A coverage report can be generated using `coverage run -m unittest` and then running `coverage html`.

