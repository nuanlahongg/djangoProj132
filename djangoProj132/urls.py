from django.contrib import admin
from django.urls import path, include
from ProfileApp import view

urlpatterns = [
    path('', view.homePage, name='homePage'),
    path('admin/', admin.site.urls),
    path('/ProfileApp/', include('ProfileApp.urls'))
]