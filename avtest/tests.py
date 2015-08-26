from django.test import TestCase
from avtest.threat import IPDetails, Reputation


class IPDetailsTestCase(TestCase):
    def setUp(self):
        self.details_good = IPDetails('8.8.8.8')
        self.details_bad  = IPDetails('69.43.161.174')

    def test_00_detail_creation(self):
        self.assertFalse(self.details_good.is_valid)
        self.assertTrue(self.details_bad.is_valid)


class ReputationTestCase(TestCase):
    def test_01_reputation(self):
        rep = Reputation.get_details('8.8.8.8')
        self.assertEqual(rep, '')
        self.assertEqual(type(rep), str)

        rep = Reputation.get_details('69.43.161.174')
        self.assertNotEqual(rep, '')
        self.assertEqual(type(rep), str)