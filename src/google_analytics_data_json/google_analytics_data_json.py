from google_analytics_data_json.create_ga4_request import Ga4Request
from google_analytics_data_json.transform_ga4_data import TransformGa4Data


def run_report_return_json(analytics_dictionary : dict = {}):
    '''
    An example analytics dictionary:
        {
            "property_id": os.environ.get("GOOGLE_ANALYTICS_PROPERTY_ID"),
            "metric_names": ["totalUsers"],
            "dimension_names": ["deviceCategory", "date", "country"],
            "order_by_names": [
                {"type": "dimension", "value": "date", "descending": False},
                {"type": "metric", "value": "totalUsers", "descending": True},
            ],
            "date_range_values":[{"start_date": "2022-05-31", "end_date": "2022-06-02"}]
        }
    '''
    
    request = Ga4Request(
        property_id=analytics_dictionary["property_id"], 
        dimension_names=analytics_dictionary["dimension_names"], 
        metric_names=analytics_dictionary["metric_names"], 
        order_by_names=analytics_dictionary["order_by_names"], 
        date_range_values=analytics_dictionary["date_range_values"]
    )
    request.create_internal_properties()
    request.run_report()

    transform_data = TransformGa4Data(google_analytics_response=request.response)
    transform_data.generate_dict()

    return transform_data.transformed_data
