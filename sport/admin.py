from django.contrib import admin
from sport.models import Field, Company, Reservation, Bill
# Register your models here.


#admin.site.register(Field)
#admin.site.register(Company)
#admin.site.register(Bill)
#admin.site.register(Reservation)


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'date', 'token')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('company', 'status', 'type', 'price')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('company_reserve', 'customer_reserve', 'field_reserve', 'schedule_date', 'schedule_time')






"""
@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('status', 'type', 'price')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('field', 'name', 'address', 'phone', 'email')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'field', 'schedule')


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'date', 'token')
"""