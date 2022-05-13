from django.shortcuts import render
from django.http import JsonResponse
from .core.Dianping import Dianping

dianping = Dianping()

def index(request):
    return render(request, 'index.html')


def get_hotel_details(request):
    url = request.GET.get('url')
    res = dianping.get_hotel_info(url=url)
    return JsonResponse(res)