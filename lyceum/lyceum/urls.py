from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("", include("homepage.urls")),
    path("catalog/", include("catalog.urls")),
    path("about/", include("about.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    # Добавить к списку urlpatterns список адресов
    # из приложения debug_tollbar:
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
