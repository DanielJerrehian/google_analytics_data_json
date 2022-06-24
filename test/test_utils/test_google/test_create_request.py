import unittest
from google.analytics.data_v1beta.types import Dimension, Metric

from src.utils.google.create_request import Client, Request


class TestClient(unittest.TestCase):
    def setUp(self):
        pass

    def test_class_object(self):
        class_object = Client
        self.assertTrue(class_object)

    def test_class_variables(self):
        class_object = Client()
        self.assertEqual(class_object.client, None)
    
    def test_create_client_method(self):
        class_object = Client()
        class_object.create_client()
        self.assertTrue(class_object.client)


class TestCreateRequest(unittest.TestCase):
    def setUp(self):
        pass

    def test_class_object(self):
        class_object = Request
        self.assertTrue(class_object)

    def test_class_variables(self):
        class_object = Request()
        self.assertEqual(class_object.client, None)
        self.assertEqual(class_object.property_id, "314724906")
        self.assertEqual(class_object.metric_names, [])
        self.assertEqual(class_object.dimension_names, [])
        self.assertEqual(class_object.start_date, None)
        self.assertEqual(class_object.end_date, "today")
        self.assertEqual(class_object.request, None)
        self.assertEqual(class_object.request, None)

    def test_pass_args(self):
        class_object = Request(property_id="abc", metric_names=["test_metric"], dimension_names=["test_dimension"], start_date="2020-03-31", end_date="2021-03-31")
        self.assertEqual(class_object.client, None)
        self.assertEqual(class_object.property_id, "abc")
        self.assertEqual(class_object.metric_names, ["test_metric"])
        self.assertEqual(class_object.dimension_names, ["test_dimension"])
        self.assertEqual(class_object.start_date, "2020-03-31")
        self.assertEqual(class_object.end_date, "2021-03-31")
        self.assertEqual(class_object.request, None)
        self.assertEqual(class_object.request, None)

    def test_pass_args_multiple_dimensions(self):
        class_object = Request(property_id="abc", metric_names=["test_metric"], dimension_names=["test_dimension", "test_dimension_2"], start_date="2020-03-31", end_date="2021-03-31")
        self.assertEqual(class_object.client, None)
        self.assertEqual(class_object.property_id, "abc")
        self.assertEqual(class_object.metric_names, ["test_metric"])
        self.assertEqual(class_object.dimension_names, ["test_dimension", "test_dimension_2"])
        self.assertEqual(class_object.start_date, "2020-03-31")
        self.assertEqual(class_object.end_date, "2021-03-31")
        self.assertEqual(class_object.request, None)
        self.assertEqual(class_object.request, None)

    def test_create_dimensions_method_single_dimension(self):
        class_object = Request(property_id="abc", metric_names=["test_metric"], dimension_names=["test_dimension"], start_date="2020-03-31", end_date="2021-03-31")
        class_object.create_dimensions()
        self.assertEqual(class_object.dimensions, [Dimension(name="test_dimension")])
    
    def test_create_dimensions_method_multiple_dimensions(self):
        class_object = Request(property_id="abc", metric_names=["test_metric"], dimension_names=["test_dimension", "test_dimension_2"], start_date="2020-03-31", end_date="2021-03-31")
        class_object.create_dimensions()
        self.assertEqual(class_object.dimensions, [Dimension(name="test_dimension"), Dimension(name="test_dimension_2")])

    def test_create_metrics_method_one_metric(self):
        class_object = Request(property_id="abc", metric_names=["test_metric"], dimension_names=["test_dimension", "test_dimension_2"], start_date="2020-03-31", end_date="2021-03-31")
        class_object.create_metrics()
        self.assertEqual(class_object.metrics, [Metric(name="test_metric")])

    def test_create_metrics_method_multiple_metrics(self):
        class_object = Request(property_id="abc", metric_names=["test_metric", "test_metric_2"], dimension_names=["test_dimension", "test_dimension_2"], start_date="2020-03-31", end_date="2021-03-31")
        class_object.create_metrics()
        self.assertEqual(class_object.metrics, [Metric(name="test_metric"), Metric(name="test_metric_2")])

    def test_create_request_method(self):
        class_object = Request(metric_names=["activeUsers"], dimension_names=["city"], start_date="2020-03-31", end_date="2021-03-31")
        class_object.create_client()
        class_object.create_dimensions()
        class_object.create_metrics()
        class_object.create_request()
        self.assertTrue(class_object.client)
        self.assertTrue(class_object.request)

    def test_run_report_method_active_users_by_country_by_date(self):
        class_object = Request(metric_names=["activeUsers"], dimension_names=["country", "date"], start_date="2022-05-31", end_date="2022-06-02")
        class_object.create_client()
        class_object.create_dimensions()
        class_object.create_metrics()
        class_object.create_request()
        class_object.run_report()
        self.assertEqual(class_object.response.row_count, 9)

    def test_run_report_method_sessions_per_user(self):
        class_object = Request(metric_names=["sessionsPerUser"], dimension_names=["date"], start_date="2022-05-31", end_date="2022-06-02")
        class_object.create_client()
        class_object.create_dimensions()
        class_object.create_metrics()
        class_object.create_request()
        class_object.run_report()
        self.assertEqual(class_object.response.row_count, 3)

    def test_run_report_method_event_count_by_event_name(self):
        class_object = Request(metric_names=["eventCount"], dimension_names=["eventName", "browser", "date"], start_date="2022-05-31", end_date="2022-06-02")
        class_object.create_client()
        class_object.create_dimensions()
        class_object.create_metrics()
        class_object.create_request()
        class_object.run_report()
        self.assertEqual(class_object.response.row_count, 62)
        self.assertEqual(class_object.response.rows[0].metric_values[0].value, "184")

    def test_run_report_method_multiple_metrics_multiple_dimensions(self):
        class_object = Request(metric_names=["activeUsers", "newUsers"], dimension_names=["browser", "date"], start_date="2022-05-31", end_date="2022-06-01")
        class_object.create_client()
        class_object.create_dimensions()
        class_object.create_metrics()
        class_object.create_request()
        class_object.run_report()
        self.assertEqual(class_object.response.row_count, 8)
        self.assertEqual(class_object.response.rows[0].metric_values[0].value, "10")