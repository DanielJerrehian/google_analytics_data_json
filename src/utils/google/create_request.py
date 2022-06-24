from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, Dimension, Metric, DateRange, OrderBy


class Client:
    def __init__(self):
        self.client = None

    def create_client(self):
        self.client = BetaAnalyticsDataClient()


class Request(Client):
    def __init__(self, property_id : str = None, dimension_names : list = [], metric_names : list = [], order_by_names : list = [], start_date : str = None, end_date : str = "today"):
        super().__init__()
        self.property_id = property_id
        self.dimension_names = dimension_names
        self.metric_names = metric_names
        self.order_by_names = order_by_names
        self.start_date = start_date
        self.end_date = end_date
        self.dimensions = []
        self.metrics = []
        self.order_bys = []
        self.request = None
        self.response = None

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

    def create_request(self):
        self.request = RunReportRequest(
            property=f"properties/{self.property_id}",
            dimensions=self.dimensions,
            metrics=self.metrics,
            order_bys=self.order_bys,
            date_ranges=[DateRange(start_date=self.start_date, end_date=self.end_date)]
        )

    def run_report(self):
        self.response = self.client.run_report(request=self.request)



