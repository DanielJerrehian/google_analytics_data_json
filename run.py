from src.main import main
from src.utils.google.create_request import create_dimension_order_by, create_metric_order_by

def run():
    
    
    # func_config = {
    #     "dimension": create_dimension_order_by(order_by_value=),
    #     "metric": create_metric_order_by(order_by_value=)
    # }
    
    
    
    main(metric_object=
        {
            "property_id": "314724906", 
            "metric_names": ["totalUsers"], 
            "dimension_names": ["country", "date"], 
            "order_by_names": [
                {
                    "type": "dimension",
                    "value": "date",
                    "function": create_dimension_order_by(order_by_value="date"),
                    # "function": func_config["dimension"],
                    "descending": False
                },
                {
                    "type": "metric",
                    "value": "totalUsers",
                    "function": create_metric_order_by(order_by_value="totalUsers"),
                    "descending": True
                }
            ], 
            "start_date": "2022-06-17"
        }
    )
    

run()
