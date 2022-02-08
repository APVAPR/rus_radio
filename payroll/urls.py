from django.urls import path

from .views import payroll, index


urlpatterns = [
    path('', index, name='index'),
    path('payroll/', payroll, name='payroll')
]