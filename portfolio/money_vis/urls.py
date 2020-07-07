from django.urls import path
from . import views

app_name = 'money_vis'
urlpatterns = [
    # /money_vis
    path('', views.index, name='index'),
]
