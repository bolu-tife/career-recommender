
from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.test, name="test"),
    path('result/', views.result, name="result"),
    path('take/', views.take, name='take'),
    path('take/save/', views.save, name='save'),


]
