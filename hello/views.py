from django.http import HttpResponse

from rest_framework.decorators import api_view
from two1.bitserv.django import payment


@api_view(['GET'])
@payment.required(100)
def buy(request):
    return HttpResponse('Hello 21!', status=200)
