from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_profile, name='add_profile'),
    path('stats/', views.stats, name='stats'),
    path('students/', views.student_list_view, name='student_list')
]
