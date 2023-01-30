from django.urls import path
from ProfileApp import view

urlpatterns = [
    path('test/', view.test, name='test'),
    path('homePage/', view.homePage, name='homePage'),
    path('secondPage/', view.secondPage, name='secondPage'),
    path('thirdPage/', view.thirdPage, name='thirdPage'),
    path('fourthPage/', view.fourthPage, name='fourthPage'),
    path('fivePage/', view.fivePage, name='fivePage'),
    path('sixthPage/', view.sixthPage, name='sixthPage'),
    path('product/', view.product, name='product'),
    path('showMyData/', view.showMyData, name='showMyData'),

]
