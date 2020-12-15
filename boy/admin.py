from django.contrib import admin

# Register your models here.

from .models import Dog, Medication, Feed, Review

admin.site.register([Dog, Medication, Feed, Review])
