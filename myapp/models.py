from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.SmallIntegerField(verbose_name="Employee ID")
    ename = models.CharField(max_length=30, verbose_name="Employee Name")
    salary = models.DecimalField(decimal_places=2, max_digits=7)
    def __str__(self):
        return self.ename