from django.http import HttpResponse

__all__ = ["home"]


def home(request):
    return HttpResponse("Главная")
