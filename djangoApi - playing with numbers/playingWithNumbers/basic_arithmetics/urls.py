from django.urls import path
from basic_arithmetics import views

# Urls pattern has been set for the basic_arithmetics app manually

urlpatterns = [
    path('total/', view=views.total, name='total'),
    path('avg/', view=views.average, name='average'),
    path('product/', view=views.product, name='product'),
]
