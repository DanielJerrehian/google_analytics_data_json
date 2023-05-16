import unittest
import os
from google.analytics.data_v1beta.types import Dimension, Metric, OrderBy, DateRange

from src.google_analytics_data_json.create_ga4_request import Ga4Client, Ga4Request

from datetime import datetime, timedelta
start_date = (datetime.utcnow() - timedelta(days=30)).strftime('%Y-%m-%d')
end_date = (datetime.utcnow() - timedelta(days=1)).strftime('%Y-%m-%d')

class TestClient(unittest.TestCase):
    def setUp(self):
        pass

    def test_class_object(self):
        class_object = Ga4Client
        self.assertTrue(class_object)

    def test_create_client_method(self):
        class_object = Ga4Client()
        self.assertTrue(class_object.client)


class TestCreateRequest(unittest.TestCase):
    def setUp(self):
        self.property_id = os.environ.get("GOOGLE_ANALYTICS_PROPERTY_ID")

    def test_class_object(self):
        class_object = Ga4Request
        self.assertTrue(class_object)

    def test_class_variables(self):
        class_object = Ga4Request()
        self.assertEqual(class_object.property_id, None)
        self.assertEqual(class_object.dimension_names, [])
        self.assertEqual(class_object.metric_names, [])
        self.assertEqual(class_object.order_by_names, [])
        self.assertEqual(class_object.date_range_values, [])
        self.assertEqual(class_object.dimensions, [])
        self.assertEqual(class_object.metrics, [])
        self.assertEqual(class_object.order_bys, [])
        self.assertEqual(class_object.date_ranges, [])
        self.assertEqual(class_object.request, None)
        self.assertEqual(class_object.request, None)

    def test_pass_args(self):
        class_object = Ga4Request(property_id="abc", dimension_names=["date"], metric_names=["totalUsers"], order_by_names=[{"type": "dimension", "value": "date", "descending": False}], date_range_values=[{"start_date": start_date, "end_date": end_date}])
        self.assertEqual(class_object.property_id, "abc")
        self.assertEqual(class_object.dimension_names, ["date"])
        self.assertEqual(class_object.metric_names, ["totalUsers"])
        self.assertEqual(class_object.order_by_names, [{"type": "dimension", "value": "date", "descending": False}])
        self.assertEqual(class_object.date_range_values, [{"start_date": start_date, "end_date": end_date}])
        self.assertEqual(class_object.request, None)

    def test_pass_args_multiple_metrics_dimensions_order_by(self):
        class_object = Ga4Request(property_id="abc", dimension_names=["date", "country"], metric_names=["activeUsers"], order_by_names=[{"type": "metrics", "value": "activeUsers", "descending": False}], date_range_values=[{"start_date": start_date, "end_date": end_date}])
        self.assertEqual(class_object.property_id, "abc")
        self.assertEqual(class_object.dimension_names, ["date", "country"])
        self.assertEqual(class_object.metric_names, ["activeUsers"])
        self.assertEqual(class_object.order_by_names, [{"type": "metrics", "value": "activeUsers", "descending": False}])
        self.assertEqual(class_object.dimensions, [])
        self.assertEqual(class_object.metrics, [])
        self.assertEqual(class_object.order_bys, [])
        self.assertEqual(class_object.date_ranges, [])
        self.assertEqual(class_object.request, None)
        self.assertEqual(class_object.request, None)

    def test_create_dimensions_method_single(self):
        class_object = Ga4Request(dimension_names=["date"])
        class_object.create_dimensions()
        self.assertEqual(class_object.dimensions, [Dimension(name="date")])

    def test_create_dimensions_method_multiple(self):
        class_object = Ga4Request(dimension_names=["country", "date"])
        class_object.create_dimensions()
        self.assertEqual(class_object.dimensions, [Dimension(name="country"), Dimension(name="date")])

    def test_create_metrics_method_single(self):
        class_object = Ga4Request(metric_names=["totalUsers"])
        class_object.create_metrics()
        self.assertEqual(class_object.metrics, [Metric(name="totalUsers")])

    def test_create_metrics_method_multiple(self):
        class_object = Ga4Request(metric_names=["totalUsers", "activeUsers"])
        class_object.create_metrics()
        self.assertEqual(class_object.metrics, [Metric(name="totalUsers"), Metric(name="activeUsers")])

    def test_create_order_by_method_single(self):
        class_object = Ga4Request(order_by_names=[{"type": "dimension", "value": "date", "descending": True}])
        class_object.create_order_bys()
        self.assertEqual(class_object.order_bys, [OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name="date"), desc=True)])

    def test_create_order_by_method_multiple(self):
        class_object = Ga4Request(order_by_names=[{"type": "dimension", "value": "date", "descending": False}, {"type": "dimension", "value": "country", "descending": True}, {"type": "metric", "value": "totalUsers", "descending": False}])
        class_object.create_order_bys()
        self.assertEqual(class_object.order_bys, [OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name="date")), OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name="country"), desc=True), OrderBy(metric=OrderBy.MetricOrderBy(metric_name="totalUsers"))])

    def test_create_date_ranges_single(self):
        class_object = Ga4Request(date_range_values=[{"start_date": start_date, "end_date": end_date}])
        class_object.create_date_ranges()
        self.assertEqual(class_object.date_ranges, [DateRange(start_date=start_date, end_date=end_date)])
        
    def test_create_date_ranges_multiple(self):
        class_object = Ga4Request(date_range_values=[{"start_date": "2022-06-31", "end_date": "2022-07-01"}, {"start_date": "2022-07-04", "end_date": "2022-07-10"}])
        class_object.create_date_ranges()
        self.assertEqual(class_object.date_ranges, [DateRange(start_date="2022-06-31", end_date="2022-07-01"), DateRange(start_date="2022-07-04", end_date="2022-07-10")])

    def test_create_request_method(self):
        class_object = Ga4Request(property_id=self.property_id, dimension_names=["city"], metric_names=["activeUsers"], date_range_values=[{"start_date": start_date, "end_date": end_date}])
        class_object.create_dimensions()
        class_object.create_metrics()
        class_object.create_order_bys()
        class_object.create_request()
        self.assertTrue(class_object.client)
        self.assertTrue(class_object.request)

    def test_run_report_method_active_users_by_country_by_date(self):
        class_object = Ga4Request(property_id=self.property_id, dimension_names=["country", "date"], metric_names=["activeUsers"], order_by_names=[{"type": "dimension", "value": "date", "descending": False}], date_range_values=[{"start_date": start_date, "end_date": end_date}])
        class_object.create_dimensions()
        class_object.create_metrics()
        class_object.create_order_bys()
        class_object.create_date_ranges()
        class_object.create_request()
        class_object.run_report()
        self.assertEqual(class_object.response.row_count, 9)

    def test_run_report_method_sessions_per_user(self):
        class_object = Ga4Request(property_id=self.property_id, dimension_names=["date"], metric_names=["sessionsPerUser"], order_by_names=[{"type": "dimension", "value": "date", "descending": False}], date_range_values=[{"start_date": start_date, "end_date": end_date}])
        class_object.create_dimensions()
        class_object.create_metrics()
        class_object.create_order_bys()
        class_object.create_date_ranges()
        class_object.create_request()
        class_object.run_report()
        self.assertEqual(class_object.response.row_count, 3)

    def test_run_report_method_event_count_by_event_name(self):
        class_object = Ga4Request(property_id=self.property_id, dimension_names=["eventName", "browser", "date"], metric_names=["eventCount"], order_by_names=[], date_range_values=[{"start_date": start_date, "end_date": end_date}])
        class_object.create_dimensions()
        class_object.create_metrics()
        class_object.create_order_bys()
        class_object.create_date_ranges()
        class_object.create_request()
        class_object.run_report()
        self.assertEqual(class_object.response.row_count, 62)
        self.assertEqual(class_object.response.rows[0].metric_values[0].value, "184")

    def test_run_report_method_multiple_metrics_multiple_dimensions(self):
        class_object = Ga4Request(property_id=self.property_id, dimension_names=["browser", "date"], metric_names=["activeUsers", "newUsers"], order_by_names=[{"type": "dimension", "value": "date", "descending": False}], date_range_values=[{"start_date": start_date, "end_date": end_date}])
        class_object.create_dimensions()
        class_object.create_metrics()
        class_object.create_order_bys()
        class_object.create_date_ranges()
        class_object.create_request()
        class_object.run_report()
        self.assertEqual(class_object.response.row_count, 8)
        self.assertEqual(class_object.response.rows[0].metric_values[0].value, "10")
