from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='pages/', blank=True, null=True)

    def __str__(self):
        return self.title


class ContactPerson(models.Model):
    ROLE_CHOICES = [
        ('head', 'Академический руководитель'),
        ('manager', 'Менеджер'),
    ]

    full_name = models.CharField("ФИО", max_length=100)
    photo = models.ImageField("Фото", upload_to='people/')
    email = models.EmailField("Электронная почта")
    phone = models.CharField("Телефон", max_length=20, blank=True)
    role = models.CharField("Роль", max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.get_role_display()}: {self.full_name}"


class StudyProgram(models.Model):
    name = models.CharField("Название ОП", max_length=200)
    url = models.URLField("Ссылка на ОП")
    description = models.TextField("Что я буду изучать / чему научусь / преимущества / перспективы")

    def __str__(self):
        return self.name


class Classmate(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    photo = models.ImageField("Фото", upload_to="classmates/")
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Электронная почта", blank=True)

    def __str__(self):
        return self.full_name


class AboutMe(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    email = models.EmailField("Электронная почта")
    phone = models.CharField("Телефон", max_length=20)
    photo = models.ImageField("Фото", upload_to='about_me/')
    resume = models.TextField("Резюме")

    def __str__(self):
        return self.full_name
