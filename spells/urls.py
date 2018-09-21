from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_spells, name='allblogs'),
    path('<str:spell_id>/', views.detail, name='detail'),
]