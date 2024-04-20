from django.http import HttpResponse

__all__ = ["description"]


def description(request):
    return HttpResponse("О проекте")
