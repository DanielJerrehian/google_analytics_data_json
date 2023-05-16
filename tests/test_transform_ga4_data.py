import unittest
import os

from src.google_analytics_data_json.transform_ga4_data import TransformGa4Data
from src.google_analytics_data_json.create_ga4_request import Ga4Request

from datetime import datetime, timedelta
start_date = (datetime.utcnow() - timedelta(days=30)).strftime('%Y-%m-%d')
end_date = (datetime.utcnow() - timedelta(days=1)).strftime('%Y-%m-%d')

start_date_older = (datetime.utcnow() - timedelta(days=45)).strftime('%Y-%m-%d')
end_date_older = (datetime.utcnow() - timedelta(days=35)).strftime('%Y-%m-%d')


class TestTransformData(unittest.TestCase):
    def setUp(self):
        self.analytics_dictionary = {"property_id" : os.environ.get("GOOGLE_ANALYTICS_PROPERTY_ID"), "metric_names": ["activeUsers", "newUsers", "totalUsers"], "dimension_names": ["country", "date"], "order_by_names": [{"type": "dimension", "value": "date", "descending": False}],  "date_range_values": [{"start_date": start_date, "end_date": end_date}]}
        request = Ga4Request(property_id=self.analytics_dictionary["property_id"], dimension_names=self.analytics_dictionary["dimension_names"], metric_names=self.analytics_dictionary["metric_names"], order_by_names=self.analytics_dictionary["order_by_names"], date_range_values=self.analytics_dictionary["date_range_values"])
        request.create_internal_properties()
        request.run_report()
        self.google_analytics_response = request.response

    def test_class_object(self):
        class_object = TransformGa4Data
        self.assertTrue(class_object)

    def test_class_variables(self):
        class_object = TransformGa4Data()
        self.assertEqual(class_object.google_analytics_response, None)
        self.assertEqual(class_object.dimension_headers, [])
        self.assertEqual(class_object.metric_headers, [])
        self.assertEqual(class_object.transformed_data, [])

    def test_pass_arguments(self):
        class_object = TransformGa4Data(google_analytics_response=self.google_analytics_response)
        self.assertEqual(class_object.google_analytics_response, self.google_analytics_response)
        self.assertEqual(class_object.dimension_headers, [])
        self.assertEqual(class_object.metric_headers, [])
        self.assertEqual(class_object.transformed_data, [])

    def test_to_dict_method_single_date_range(self):
        class_object = TransformGa4Data(google_analytics_response=self.google_analytics_response)
        class_object.generate_dict()
        self.assertEqual(class_object.transformed_data[0]["date"], start_date.replace('-',''))
        
    def test_to_dict_method_multiple_date_ranges(self):
        other_analytics_dictionary = {"property_id" : os.environ.get("GOOGLE_ANALYTICS_PROPERTY_ID"), "metric_names": ["totalUsers"], "dimension_names": ["country"], "order_by_names": [{"type": "dimension", "value": "country", "descending": True}],  "date_range_values": [{"start_date": start_date_older, "end_date": end_date_older}, {"start_date": start_date, "end_date": end_date} ]}
        request = Ga4Request(property_id=other_analytics_dictionary["property_id"], dimension_names=other_analytics_dictionary["dimension_names"], metric_names=other_analytics_dictionary["metric_names"], order_by_names=other_analytics_dictionary["order_by_names"], date_range_values=other_analytics_dictionary["date_range_values"])
        request.create_internal_properties()
        request.run_report()
        other_google_analytics_response = request.response
        class_object = TransformGa4Data(google_analytics_response=other_google_analytics_response)
        class_object.generate_dict()
        self.assertEqual(class_object.transformed_data[0]['country'], "United States")
        