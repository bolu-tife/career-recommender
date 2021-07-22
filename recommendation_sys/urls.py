
from django.urls import path
from . import views


urlpatterns = [
	path('/a', views.index, name='index'),
	path('', views.indexx, name='indexx'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('studentdashboard/', views.studentdashboard, name='studentdashboard'),
    path('rankings/', views.rankings, name='rankings'),
    path('rankings_acad/', views.rankings_acad, name='rankings_acad'),
    path('rankings_pers/', views.rankings_pers, name='rankings_pers'),
    path('rankings_both/', views.rankings_both, name='rankings_both'),
    

]
