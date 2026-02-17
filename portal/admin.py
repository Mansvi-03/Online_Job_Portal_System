from django.contrib import admin
from .models import Candidate, Company, Job, Application

admin.site.register(Candidate)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Application)


