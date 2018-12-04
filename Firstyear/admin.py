from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(phySemSubject)
admin.site.register(chemSemSubject)

admin.site.register(cpQpaper)
admin.site.register(cpEbook)
admin.site.register(cpNote)
admin.site.register(cpAssignment)