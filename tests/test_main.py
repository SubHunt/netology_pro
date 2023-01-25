import unittest
from unittest import TestCase
from main1 import rus_city, geo_id, max_rate

class TestRusCity_ok(TestCase):
    def test_type_data(self):
        res = type(rus_city)
        self.assertEqual(res,list)

    @unittest.expectedFailure
    def test_type_data_2(self):
        res = type(rus_city)
        self.assertEqual(res,tuple)
    
    @unittest.expectedFailure
    def test_list_not_empty(self):
        res = rus_city
        self.assertEqual(len(res), 0)

    def test_result(self):
        res = [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 
                'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]
        self.assertEqual(res, rus_city)


class GeoID(TestCase):

    def test_not_empty(self):
        res = geo_id()
        self.assertNotEqual(len(res), 0)


    def test_result(self):
        res = [98, 35, 15, 213, 54, 119]
        self.assertEqual(res, geo_id())

class MaxRate(TestCase):

    def test_maxe_rate(self):
        res = max_rate()
        self.assertEqual(res, 'yandex')

    @unittest.expectedFailure
    def test_not_max_rate(self):
        res = max_rate()
        self.assertNotEqual(res, 'google')
    


