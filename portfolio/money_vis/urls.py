from django.urls import path

from . import views

urlpatterns = [
    # /money_vis
    path('', views.index, name='index'),
]
