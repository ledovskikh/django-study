import django.test

__all__ = ["StaticURLsTests"]


class StaticURLsTests(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = django.test.Client().get("//")
        self.assertEqual(response.status_code, 200)
