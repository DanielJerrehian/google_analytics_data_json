import unittest
from datetime import datetime, timedelta

from src.main import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.date_yesterday = (datetime.utcnow() - timedelta(days=1)).date()

    def test_function_object(self):
        function_object = main
        self.assertTrue(function_object)

    def test_main(self):
        function_object = main(metric_object={"metric_names": ["activeUsers", "newUsers"], "dimension_names": ["country", "date"]})
        self.assertTrue(function_object)
