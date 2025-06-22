from django.http import HttpResponse
from django.utils import translation

def get_language(request):
    return HttpResponse(translation.get_language())
