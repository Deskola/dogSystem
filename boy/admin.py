from django.contrib import admin

# Register your models here.

from .models import Dog, Medication, Feed, Review, MedicationForAll

admin.site.register([Dog, Medication, MedicationForAll, Feed, Review])
