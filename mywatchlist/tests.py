from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class TestCaseForMyWatchList(TestCase):
    def test_html_form(self):
        resp = Client().get('/mywatchlist/html/')
        self.assertEqual(resp.status_code, 200)
        
    def test_xml_form(self):
        resp = Client().get('/mywatchlist/xml/')
        self.assertEqual(resp.status_code, 200)

    def test_json_form(self):
        resp = Client().get('/mywatchlist/json/')
        self.assertEqual(resp.status_code, 200)
