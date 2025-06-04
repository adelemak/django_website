from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_me_view, name='about_me'),
    path('program/', views.study_program_view, name='study_program'),
    path('management/', views.management_view, name='management'),
    path('classmates/', views.classmates_view, name='classmates'),
    path('<slug:slug>/', views.page_detail_view, name='page_detail')
]