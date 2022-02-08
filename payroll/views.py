from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>Стартовая страница сайта русского радио</h>')


def payroll(request):
    print(request)
    return render(request, 'payroll/payroll.html')

