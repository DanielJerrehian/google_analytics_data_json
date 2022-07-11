from src.utils.google.create_request import Request
from src.transformation.transform_data import TransformData


def main(analytics_dictionary : dict = {}):
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
    
    request = Request(
        property_id=analytics_dictionary["property_id"], 
        dimension_names=analytics_dictionary["dimension_names"], 
        metric_names=analytics_dictionary["metric_names"], 
        order_by_names=analytics_dictionary["order_by_names"], 
        date_range_values=analytics_dictionary["date_range_values"]
    )
    request.create_client()
    request.create_dimensions()
    request.create_metrics()
    request.create_order_bys()
    request.create_date_ranges()
    request.create_request()
    request.run_report()

    transform_data = TransformData(google_analytics_response=request.response)
    transform_data.to_dict()

    return transform_data.transformed_data
