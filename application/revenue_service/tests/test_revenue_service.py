from unittest.mock import patch
from flask import url_for 
from flask import Flask
from flask_testing import TestCase
from  ..revenue_service import app


class TestBase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app


class TestResponse(TestBase):

    def test_revenue(self):
        with patch('random.randint') as random:
            random.return_value = "5000" 
            response = self.client.get(url_for('get_revenue'))
            self.assertEqual(response.json,dict(Revenue='5000'))
            self.assertEqual(response.status_code, 200)