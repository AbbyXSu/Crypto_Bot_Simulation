from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
import requests_mock
from  ..app import app, db
from ..app import Reports
import unittest


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI= "sqlite:///data.db")
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Reports(revenue ="100", expense="50", PLtype="profit",income="income",efficiency_ratio ='100'))
        db.session.commit


    def tearDown(self):
        db.session.remove()
        db.drop_all()
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("get_performance"))
        self.assertEqual(response.status_code, 500)


class TestResponse(TestBase):

    def test_performance_breakeven(self):
                items=dict(revenue='500',expense='-500',PLtype='Break-even',efficiency_ratio='0',income='0')
                response = self.client.post(url_for('get_performance'), json=items)
                self.assertIn(response.json,500)
                self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()