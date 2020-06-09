from django.contrib import admin

# Register your models here.
from info.models import About, Experience, Project, CV

admin.site.register(About)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(CV)