from typing import List

class TransformGa4Data:
    def __init__(self, google_analytics_response : object = None):
        self.google_analytics_response = google_analytics_response
        self.dimension_headers = []
        self.metric_headers = []
        self.transformed_data: List[dict] = []

    def generate_dict(self):
        """ Fills `self.transformed_data` with a list of dicts. """
        for dimension_header in self.google_analytics_response.dimension_headers:
            self.dimension_headers.append(dimension_header.name)

        for metric_header in self.google_analytics_response.metric_headers:
            self.metric_headers.append(metric_header.name)
        
        for row in self.google_analytics_response.rows:
            transformed_row = {}
            for (dimension_header, dimension_value) in zip(self.dimension_headers, row.dimension_values):
                transformed_row[dimension_header] = dimension_value.value
            for (metric_header, metric_value) in zip(self.metric_headers, row.metric_values):
                transformed_row[metric_header] = metric_value.value

            self.transformed_data.append(transformed_row)
