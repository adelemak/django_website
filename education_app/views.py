from django.shortcuts import render, redirect
from .models import StudentProfile
from .forms import StudentProfileForm
from django.db.models import Avg, Count


def home(request):
    return render(request, 'education_app/home.html')


def add_profile(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_profiles')
    else:
        form = StudentProfileForm()
    return render(request, 'education_app/add_profile.html', {'form': form})


def stats(request):
    stats_data = StudentProfile.objects.values('program').annotate(
        avg_gpa=Avg('gpa'), count=Count('id')
    )
    return render(request, 'education_app/stats.html', {'stats': stats_data})


def student_list_view(request):
    sort_by = request.GET.get("sort", "last_name")
    search_query = request.GET.get("q", "")

    students = StudentProfile.objects.all()

    if search_query:
        students = students.filter(
            last_name__icontains=search_query
        )

    students = students.order_by(sort_by)

    avg_gpa = StudentProfile.objects.aggregate(avg_gpa=Avg('gpa'))["avg_gpa"]
    avg_gpa = round(avg_gpa, 2) if avg_gpa else None

    return render(request, 'education_app/students.html', {
        'students': students,
        'avg_gpa': avg_gpa,
        'sort_by': sort_by,
        'search_query': search_query,
    })