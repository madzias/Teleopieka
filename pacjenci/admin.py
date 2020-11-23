from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Dom)
admin.site.register(Asystent)
admin.site.register(Pacjent)
admin.site.register(Zgloszenie)