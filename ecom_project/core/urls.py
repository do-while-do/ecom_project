from django.urls import path, include
from ecom_project.core import views

urlpatterns = [
    path('', views.HomeDetailView.as_view(), name='home_page')
]
