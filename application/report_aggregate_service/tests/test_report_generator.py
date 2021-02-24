from unittest.mock import patch
from flask import url_for 
from flask import Flask
from sqlalchemy.sql.expression import null
from flask_testing import TestCase
from  ..report_generator import app



class TestBase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app


class TestResponse(TestBase):

    def test_performance(self):
            response = self.client.post(url_for('get_performance'))
            self.assertEqual(response.status_code, 400)

    def test_performance_breakeven(self):
                items=dict(revenue='500',expense='-500')
                response = self.client.post(url_for('get_performance'), json=items)
                
                self.assertEqual(response.json,dict(PLtype='Break-even',efficiency_ratio=0,income=0))
                self.assertEqual(response.status_code, 200)

    def test_performance_loss(self):
                items=dict(revenue='50',expense='-500')
                response = self.client.post(url_for('get_performance'), json=items)
                
                self.assertEqual(response.json,dict(PLtype='Loss',efficiency_ratio=-90,income=-450))
                self.assertEqual(response.status_code, 200)

    def test_performance_profit(self):
                items=dict(revenue='500',expense='-50')
                response = self.client.post(url_for('get_performance'), json=items)
                
                self.assertEqual(response.json,dict(PLtype='profit',efficiency_ratio=900,income=450))
                self.assertEqual(response.status_code, 200)


