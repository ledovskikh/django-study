import django.test

__all__ = ["StaticURLTests"]


class StaticURLTests(django.test.TestCase):
    def test_about_endpoint(self):
        response = django.test.Client().get("/about/")
        self.assertEqual(response.status_code, 200)
