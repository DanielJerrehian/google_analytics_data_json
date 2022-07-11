import unittest
import os

from src.google_analytics_data_json.google_analytics_data_json import run_report_return_json


class TestMain(unittest.TestCase):
    def setUp(self):
        self.analytics_dictionary = {
            "property_id": os.environ.get("GOOGLE_ANALYTICS_PROPERTY_ID"),
            "metric_names": ["totalUsers"],
            "dimension_names": ["deviceCategory", "date", "country"],
            "order_by_names": [
                {"type": "dimension", "value": "date", "descending": False},
                {"type": "metric", "value": "totalUsers", "descending": True},
            ],
            "date_range_values":[{"start_date": "2022-05-31", "end_date": "2022-06-02"}]
        }

    def test_function_object(self):
        function_object = run_report_return_json
        self.assertTrue(function_object)

    def test_main(self):
        function_object = run_report_return_json(analytics_dictionary=self.analytics_dictionary)
        self.assertTrue(function_object[0]["country"])
