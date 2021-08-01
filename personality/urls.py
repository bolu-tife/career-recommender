
from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.test, name="test"),
    path('result/', views.result, name="result"),
    path('take/', views.take, name='take'),
    path('take/save/', views.save, name='save'),
    path('testtwo/', views.testtwo, name='testtwo'),
    path('testtwo/testtwosave/', views.testtwosave, name='testtwosave'),
    


]
