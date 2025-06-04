from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class StudentProfile(models.Model):
    COURSE_CHOICES = [
        (1, "1 курс"),
        (2, "2 курс"),
        (3, "3 курс"),
        (4, "4 курс"),
        (5, "5 курс"),
    ]

    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    course = models.IntegerField("Курс", choices=COURSE_CHOICES)
    program = models.CharField("Образовательная программа", max_length=100)
    gpa = models.DecimalField(
        "Средний балл (GPA)",
        max_digits=3, decimal_places=1,
        validators=[MinValueValidator(0.0)]
    )
    email = models.EmailField("Электронная почта")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"