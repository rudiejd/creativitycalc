from django.urls import path
from . import views
from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    path('', views.index, name ='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('calculate/', views.calculate, name='calculate'),
]