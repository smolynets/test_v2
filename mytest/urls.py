from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:test_id>/test/', views.one_test, name='one_test'),
]