import yaml

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from two1.bitserv.django import payment

from hello import settings


@api_view(['GET'])
@payment.required(100)
def buy(request):
    return HttpResponse('Hello 21!', status=200)


@api_view(['GET'])
def manifest(request):
    with open(settings.BASE_DIR + "/hello/manifest.yaml", 'r') as infile:
        return JsonResponse(yaml.load(infile), status=200)
