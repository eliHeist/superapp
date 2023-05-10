from projects.models import FeaturedProject, Photo, Project
from django.contrib import admin

# Register your models here.
admin.site.register(Project)
admin.site.register(FeaturedProject)
admin.site.register(Photo)