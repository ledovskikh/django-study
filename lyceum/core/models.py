import django.db

__all__ = ["CommonInfo"]


class CommonInfo(django.db.models.Model):
    name = django.db.models.CharField(max_length=150, verbose_name="Название")
    # id = django.db.models.BigAutoField(primary_key=True, verbose_name="id")
    is_published = django.db.models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
    )

    class Meta:
        abstract = True
