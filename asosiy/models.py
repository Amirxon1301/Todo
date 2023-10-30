from django.db import models

class Student(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.SmallIntegerField()
    kurs = models.SmallIntegerField()
    student_raqami = models.SmallIntegerField(unique=True)

class Reja(models.Model):
    sarlavha = models.CharField(max_length=30)
    sana = models.DateField()
    batafsil_malumot = models.TextField(null=True, blank=True)
    bajarilgan = models.BooleanField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

