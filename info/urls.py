
from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<int:id>/', views.details, name='details'),
]