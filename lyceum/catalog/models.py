import django.db
from lyceum.core.models import CommonInfo

__all__ = ["CatalogItem"]


class CatalogItem(CommonInfo):
    text = django.db.models.TextField(verbose_name="Текст")

    class Meta:
        db_table = "catalog_item"
