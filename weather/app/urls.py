
from . import views
from django.urls import path

urlpatterns = [
    path('',views.base,name='base'),
]
