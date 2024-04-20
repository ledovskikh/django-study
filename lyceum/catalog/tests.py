import django.test
import parameterized

__all__ = ["CatalogTestCase"]


class CatalogTestCase(django.test.TestCase):
    def test_catalog_endpoint(self):
        response = django.test.Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    @parameterized.parameterized.expand(
        [
            ("0", 200),
            ("1", 200),
            ("100500", 200),
            ("-0", 404),
            ("-1", 404),
            ("-12345", 404),
            ("34.344", 404),
            ("hello", 404),
            ("he11wo1d", 404),
            ("__main__", 404),
            ("1^54%", 404),
        ],
    )
    def test_catalog_item_endpoint(self, url, expected_status_code):
        response = django.test.Client().get(f"/catalog/{url}/")
        self.assertEqual(response.status_code, expected_status_code)
