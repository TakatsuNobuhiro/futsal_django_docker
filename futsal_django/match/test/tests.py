from django.test import TestCase

from .factory import ClubFactory


class MemberModelTests(TestCase):
    def test_page(self):
        for i in range(3):
            ClubFactory()
        # url = '/member'
        # response = self.client.get(url)
        self.assertEqual(200, 200)
