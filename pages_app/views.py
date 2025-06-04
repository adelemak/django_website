from django.shortcuts import render, get_object_or_404
from .models import Page, ContactPerson, StudyProgram, Classmate, AboutMe


def home_view(request):
    return render(request, 'pages_app/home.html')


def about_me_view(request):
    about = AboutMe.objects.first()  # предполагаем, что запись одна
    return render(request, 'pages_app/about_me.html', {'about': about})


def study_program_view(request):
    program = StudyProgram.objects.first()
    return render(request, 'pages_app/study_program.html', {'program': program})


def management_view(request):
    staff = ContactPerson.objects.all()
    return render(request, 'pages_app/management.html', {'staff': staff})


def classmates_view(request):
    classmates = Classmate.objects.all()
    return render(request, 'pages_app/classmates.html', {'classmates': classmates})


def page_detail_view(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'pages_app/page.html', {'page': page})
