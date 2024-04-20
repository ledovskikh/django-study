# Generated by Django 4.2.10 on 2024-03-04 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_catalogitem_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="catalogcategory",
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterModelOptions(
            name="catalogitem",
            options={"verbose_name": "Товар", "verbose_name_plural": "Товары"},
        ),
        migrations.AlterModelOptions(
            name="catalogtag",
            options={"verbose_name": "Тег", "verbose_name_plural": "Теги"},
        ),
    ]