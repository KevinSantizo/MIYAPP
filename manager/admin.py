from django.contrib import admin
from manager.models import Manager
# Register your models here.


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'address', 'password')