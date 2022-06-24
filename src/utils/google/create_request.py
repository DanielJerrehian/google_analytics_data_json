from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, Dimension, Metric, DateRange, OrderBy


class Client:
    def __init__(self):
        self.client = None

    def create_client(self):
        self.client = BetaAnalyticsDataClient()


class Request(Client):
    def __init__(self, property_id : str = "314724906", metric_names : list = [], dimension_names : list = [], order_by : str = "date", start_date : str = None, end_date : str = "today"):
        super().__init__()
        self.property_id = property_id
        self.dimension_names = dimension_names
        self.metric_names = metric_names
        self.order_by = order_by
        self.start_date = start_date
        self.end_date = end_date
        self.dimensions = []
        self.metrics = []
        self.request = None
        self.response = None

    def create_dimensions(self):
        for dimension in self.dimension_names:
            self.dimensions.append(Dimension(name=dimension))
        
    def create_metrics(self):
        for metric in self.metric_names:
            self.metrics.append(Metric(name=metric))

    def create_request(self):
        self.request = RunReportRequest(
            property=f"properties/{self.property_id}",
            dimensions=self.dimensions,
            metrics=self.metrics,
            order_bys=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name=self.order_by))],
            date_ranges=[DateRange(start_date=self.start_date, end_date=self.end_date)]
        )

    def run_report(self):
        self.response = self.client.run_report(request=self.request)

