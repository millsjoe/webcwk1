from django.contrib import admin
from modules.models import LecturerInfo, ModuleInfo, Rating

admin.site.register(ModuleInfo)
admin.site.register(LecturerInfo)
admin.site.register(Rating)
# Register your models here.
