from unittest.mock import patch
from flask import url_for 
from flask import Flask
from flask_testing import TestCase
from ..expenditure_service import app


class TestBase(TestCase):
    def create_app(self):
        #app = Flask(__name__)
        app.config['TESTING'] = True
        return app


class TestResponse(TestBase):

    def test_expenditure(self):
        with patch('random.randint') as random:
            random.return_value = "-500" 
            response = self.client.get(url_for('get_expenditrue'))
            self.assertEqual(response.json,dict(Expense='-500'))
            self.assertEqual(response.status_code, 200)