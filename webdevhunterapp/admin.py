from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Developer)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Reply)