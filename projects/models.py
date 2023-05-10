from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator 

def current_year():     
    return datetime.date.today().year 

def max_value_current_year(value):     
    return MaxValueValidator(current_year())(value)     

# Create your models here.
class Project(models.Model):
    STATUSES = (
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed')
    )
    name = models.CharField(max_length=200)
    client = models.CharField(max_length=100)
    year = models.IntegerField(('year'), validators=[MinValueValidator(2010), max_value_current_year]) 
    status = models.CharField(max_length=10, choices=STATUSES)
    picture = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField()
    slide = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.project.name} photo"


class FeaturedProject(models.Model):
    project = models.ForeignKey('Project', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.project:
            return 'self.project.name'
        else:
            return 'UNASIGNED'