from django.db import models
# from django.urls import reverse


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10,default="None")
    course = models.CharField(max_length=100,default="None")
    age = models.IntegerField()
    
    # def get_absolute_url(self):
    #     return reverse("student_list", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} is  {self.age} years old"
