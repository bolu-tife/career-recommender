
from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.test, name="test"),
    path('result/', views.result, name="result"),
    path('fisa/', views.fisa, name='fisa'),
    path('fisa/save/', views.save, name='save'),


]
