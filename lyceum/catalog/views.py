from django.http import HttpResponse

__all__ = ["item_detail", "item_list"]


def item_list(request):
    return HttpResponse("Список элементов")


def item_detail(request, elem):
    return HttpResponse("Подробно элемент")
