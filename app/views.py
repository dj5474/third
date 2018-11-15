from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from app.models import Address


def list(request):
    address = Address.objects.all()
    return HttpResponse(address)

def index(request):
    address = ''
    try:
        address = request.GET['address']

        # DB insert           내가 생성한 변수
        add = Address(address=address)
                    # 클래스가 가지고 있는 변수
        add.save() # save >> Model에서 상속받은 method

    except MultiValueDictKeyError:
        pass
    return HttpResponse('{"Hello": "'\
                        + address + '"}')

