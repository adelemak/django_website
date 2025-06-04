from django.contrib import admin
from .models import Page, ContactPerson, StudyProgram, Classmate, AboutMe


admin.site.register(Page)
admin.site.register(ContactPerson)
admin.site.register(StudyProgram)
admin.site.register(Classmate)
admin.site.register(AboutMe)
