from flask import url_for 
from flask import Flask
from sqlalchemy.sql.expression import null, text
from flask_testing import TestCase
from  ..app import app
import requests, unittest
from unittest import mock


class TestBase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://report_engine:5004/report_engine':
        return MockResponse(
            {
                "latest_item": {'revenue':'-500','expense':'-500','income':'-1000','PLtype':'Loss','efficiency_ratio':'-200'},
                "reports": [
                    {'revenue':'-500','expense':'-500','income':'-1000','PLtype':'Loss','efficiency_ratio':'-200'},
                    {'revenue':'500','expense':'-50','income':'450','PLtype':'profit','efficiency_ratio':'900'}
                ]
            }, 200
        )

    return MockResponse(None, 404)


class UITestCase(TestBase):
    # patch 'requests.get' with own method. The mock object is passed in to test case method.
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_index(self, mock_get):
        response  = self.client.get(url_for('index'))
        #assert that your html is correct
        self.assertIn(b'Loss',response.data) 
        self.assertIn(b'profit',response.data) 
        self.assertEqual (response.status_code, 200)

    @mock.patch('requests.get', side_effect=None)
    def test_index_none(self, mock_get):
        response  = self.client.get(url_for('index'))
        self.assertEqual (response.status_code,200)


if __name__ == '__main__':
    unittest.main()