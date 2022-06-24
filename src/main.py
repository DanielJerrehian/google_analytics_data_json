from dotenv import load_dotenv
from pprint import pprint

from src.utils.google.create_request import Request
from src.transformation.transform_data import TransformData


def main(metric_object):
    load_dotenv(".env")

    request = Request(property_id=metric_object["property_id"], dimension_names=metric_object["dimension_names"], metric_names=metric_object["metric_names"], order_by_names=metric_object["order_by_names"], start_date=metric_object["start_date"])
    request.create_client()
    request.create_dimensions()
    request.create_metrics()
    request.create_order_bys()
    request.create_request()
    request.run_report()
    
    transform_data = TransformData(metric_dict=metric_object, google_analytics_response=request.response)
    transform_data.to_dict()
    
    pprint(transform_data.transformed_data)
    
    return transform_data.transformed_data

