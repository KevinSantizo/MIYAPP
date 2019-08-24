from django.contrib import admin
from sport.models import Reservation, Bill, Championship, Group, Team, Match, Result, Field, Company, AssignGroup
# Register your models here.


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('company_reserve', 'customer_reserve', 'field_reserve', 'schedule_date', 'schedule_time')


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'date', 'token')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'status', 'type', 'price')


@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    list_display = ('championship_company', 'name_championship', 'description', 'registration_price')


class AssignGroupInline(admin.TabularInline):
    model = AssignGroup


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('championship_group', 'name_group')
    inlines = [AssignGroupInline]


class AssignGroupInline(admin.TabularInline):
    model = AssignGroup


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('agent_team', 'name_team', 'players')
    inlines = [AssignGroupInline]


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team_one', 'team_two', 'description_match', 'day_played', 'time_played')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('match', 'team', 'goal_team', 'date_result')


@admin.register(AssignGroup)
class AssignGroupAdmin(admin.ModelAdmin):
    list_display = ('group', 'team')




