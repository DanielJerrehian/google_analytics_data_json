import unittest
from datetime import datetime, timedelta
import os

from src.main import main


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
        function_object = main
        self.assertTrue(function_object)

    def test_main(self):
        function_object = main(analytics_dictionary=self.analytics_dictionary)
        self.assertTrue(function_object[0]["country"])
