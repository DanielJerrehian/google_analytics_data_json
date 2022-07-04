from dotenv import load_dotenv
import os


load_dotenv(".env")

metric_object = {
    "property_id": os.environ.get("BP_BIO_LC_PRODUCTION_PROPERTY_ID"), 
    "metric_names": ["totalUsers"], 
    "dimension_names": ["deviceCategory", "date", "country"], 
    "order_by_names": [
        {
            "type": "dimension",
            "value": "date",
            "descending": False
        },
        {
            "type": "metric",
            "value": "totalUsers",
            "descending": True
        }
    ], 
    "start_date": "2022-06-17"
}
    