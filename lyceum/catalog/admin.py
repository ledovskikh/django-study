from django.contrib import admin
import catalog.models


@admin.register(catalog.models.CatalogItem)
class CatalogItemAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.CatalogItem.name.fieldname,
    )


@admin.register(catalog.models.CatalogCategory)
class CatalogCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(catalog.models.CatalogTag)
class CatalogTagAdmin(admin.ModelAdmin):
    pass
