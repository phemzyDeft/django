from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=50)


class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=11)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
