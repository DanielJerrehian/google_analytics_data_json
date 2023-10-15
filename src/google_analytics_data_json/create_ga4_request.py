from typing import Union
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, Dimension, Metric, DateRange, OrderBy
from google.oauth2 import service_account


class Ga4Client:
    def __init__(self, service_account_credentials: Union[service_account.Credentials, None] = None):
        """
        `service_account_credentials` can be created with: 
            1. `service_account.Credentials.from_service_account_info(json_file_contents_as_dict)`
            2. `service_account.Credentials.from_service_account_file(path_to_json_file)`
        """
        if service_account_credentials:
            self.client = BetaAnalyticsDataClient(credentials=service_account_credentials)
        else:
            self.client = BetaAnalyticsDataClient() # Will use credentials from GOOGLE_APPLICATION_CREDENTIALS environment variables


class Ga4Request(Ga4Client):
    def __init__(self, property_id : str = None, dimension_names : list = [], metric_names : list = [], order_by_names : list = [], date_range_values : list = [], service_account_credentials: Union[service_account.Credentials, None] = None):
        super().__init__(service_account_credentials=service_account_credentials)
        self.property_id = property_id
        self.dimension_names = dimension_names
        self.metric_names = metric_names
        self.order_by_names = order_by_names
        self.date_range_values = date_range_values
        self.dimensions = []
        self.metrics = []
        self.order_bys = []
        self.date_ranges = []
        self.request = None

    def create_dimensions(self):
        for dimension in self.dimension_names:
            self.dimensions.append(Dimension(name=dimension))
        
    def create_metrics(self):
        for metric in self.metric_names:
            self.metrics.append(Metric(name=metric))
            
    def create_order_bys(self):               
        for order_by in self.order_by_names:   
            if order_by["type"] == "metric":
                self.order_bys.append(OrderBy(metric=OrderBy.MetricOrderBy(metric_name=order_by["value"]), desc=order_by["descending"]))
            elif order_by["type"] == "dimension":
                self.order_bys.append(OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name=order_by["value"]), desc=order_by["descending"]))
                
    def create_date_ranges(self):
        for date_range in self.date_range_values:
            self.date_ranges.append(DateRange(start_date=date_range["start_date"], end_date=date_range["end_date"]))
            
    def create_request(self):
        self.request = RunReportRequest(
            property=f"properties/{self.property_id}",
            dimensions=self.dimensions,
            metrics=self.metrics,
            order_bys=self.order_bys,
            date_ranges=self.date_ranges
        )

    def create_internal_properties(self):
        self.create_dimensions()
        self.create_metrics()
        self.create_order_bys()
        self.create_date_ranges()
        self.create_request()

    def run_report(self):
        self.response = self.client.run_report(request=self.request)
