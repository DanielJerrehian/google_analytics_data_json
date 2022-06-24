import unittest

from src.transformation.transform_data import TransformData
from src.utils.google.create_request import Request


class TestTransformData(unittest.TestCase):
    def setUp(self):
        self.metric_dict = {"property_id" : "314724906", "metric_names": ["activeUsers", "newUsers"], "dimension_names": ["country", "date"], "order_by_names": [{"type": "dimension", "value": "date", "descending": False}], "start_date": "2022-06-17", "end_date": "2022-06-19"}
        request = Request(property_id=self.metric_dict["property_id"], dimension_names=self.metric_dict["dimension_names"], metric_names=self.metric_dict["metric_names"], order_by_names=self.metric_dict["order_by_names"], start_date=self.metric_dict["start_date"], end_date=self.metric_dict["end_date"])
        request.create_client()
        request.create_dimensions()
        request.create_metrics()
        request.create_order_bys()
        request.create_request()
        request.run_report()
        self.google_analytics_response = request.response

    def test_class_object(self):
        class_object = TransformData
        self.assertTrue(class_object)

    def test_class_variables(self):
        class_object = TransformData()
        self.assertEqual(class_object.metric_dict, None)
        self.assertEqual(class_object.google_analytics_response, None)
        self.assertEqual(class_object.dimension_headers, [])
        self.assertEqual(class_object.metric_headers, [])
        self.assertEqual(class_object.transformed_data, [])

    def test_pass_arguments(self):
        class_object = TransformData(metric_dict=self.metric_dict, google_analytics_response=self.google_analytics_response)
        self.assertEqual(class_object.metric_dict, self.metric_dict)
        self.assertEqual(class_object.google_analytics_response, self.google_analytics_response)
        self.assertEqual(class_object.dimension_headers, [])
        self.assertEqual(class_object.metric_headers, [])
        self.assertEqual(class_object.transformed_data, [])

    def test_to_dict_method(self):
        class_object = TransformData(metric_dict=self.metric_dict, google_analytics_response=self.google_analytics_response)
        class_object.to_dict()
        self.assertEqual(class_object.transformed_data,
            [
                {'country': 'United Kingdom', 'date': '20220617', 'activeUsers': '59', 'newUsers': '49'}, 
                {'country': 'United States', 'date': '20220617', 'activeUsers': '48', 'newUsers': '44'}, 
                {'country': 'India', 'date': '20220617', 'activeUsers': '3', 'newUsers': '0'}, 
                {'country': 'Canada', 'date': '20220617', 'activeUsers': '1', 'newUsers': '0'}, 
                {'country': 'United Kingdom', 'date': '20220618', 'activeUsers': '2', 'newUsers': '0'}, 
                {'country': 'United States', 'date': '20220618', 'activeUsers': '1', 'newUsers': '1'}, 
                {'country': 'United States', 'date': '20220619', 'activeUsers': '2', 'newUsers': '2'}, 
                {'country': 'United Kingdom', 'date': '20220619', 'activeUsers': '1', 'newUsers': '0'}
            ]
        )
        