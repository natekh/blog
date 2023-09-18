from django.urls import path
from . import views

app_name = 'writings'

urlpatterns = [
    path('', views.index, name='indexs'),
]
