import unittest
from datetime import datetime, timedelta

from src.main import main
from src.metrics.metric_object import metric_object

class TestMain(unittest.TestCase):
    def setUp(self):
        self.date_yesterday = (datetime.utcnow() - timedelta(days=1)).date()

    def test_function_object(self):
        function_object = main
        self.assertTrue(function_object)

    def test_main(self):
        function_object = main(metric_object=metric_object)
        self.assertTrue(function_object[0]["country"])
