from django.db import models
from users.models import Customer
import uuid
from django.utils import timezone


# Create your models here.

class Field(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    FIELD_STATUS = (
        ('R', 'Reserved'),
        ('A', 'Available'),
    )
    status = models.CharField(
        max_length=1,
        choices=FIELD_STATUS,
        blank=True,
        default='A',
    )

    TYPE_FIELD = (
        ('1', '5 Players'),
        ('2', '7 Players'),
        ('3', '11 Players'),
    )

    type = models.CharField(
        max_length=1,
        choices=TYPE_FIELD,
        blank=True,
        default='1',
    )

    price = models.CharField(max_length=75)

    def __str__(self):
        return ' Type Field: ' + self.type + ', Price: ' + self.price


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name + ' -- ' + self.address


class Reservation(models.Model):
    company_reserve = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    customer_reserve = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_reserve')
    field_reserve = models.ForeignKey(Field, on_delete=models.CASCADE)
    schedule_date = models.DateField(null=True)
    schedule_time = models.TimeField(null=True)

    def __str__(self):
        return 'Company: ' + self.company_reserve.name + 'Address:' + self.company_reserve.address + 'Customer: ' + self.customer_reserve.first_name + ' --- Type Field: --- ' + self.field_reserve.type + ' --- Date Reserved: --- ' \
               + str(self.schedule_date) + ' Schedule Time ' + str(self.schedule_time) + ' --- Price: --- ' + self.field_reserve.price


class Bill(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    token = models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')


class Championship(models.Model):
    championship_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name_championship = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return 'Company: ' + self.championship_company.name + ' ' + self.name_championship + ' ' + self.description


class Group(models.Model):
    championship_group = models.ForeignKey(Championship, on_delete=models.CASCADE)
    name_group = models.CharField(max_length=100)

    def __str__(self):
        return 'Championship: ' + self.championship_group.name_championship


class Team(models.Model):
    agent_team = models.OneToOneField(Customer, on_delete=models.CASCADE)
    group_team = models.ForeignKey(Group, on_delete=models.CASCADE)
    name_team = models.CharField(max_length=100)
    players = models.PositiveIntegerField()

    def __str__(self):
        return 'Agent: ' + self.agent_team.first_name + ' Group: ' + self.group_team.name_group + ' ' + self.name_team


class Match(models.Model):
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one')
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two')
    description_match = models.TextField()
    day_played = models.DateField()
    time_played = models.TimeField()

    def __str__(self):
        return 'Team One: ' + self.team_one.name_team + 'Team Two: ' + ' ' + self.team_two.name_team


class Result(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    goal_team = models.PositiveIntegerField()
    date_result = models.DateField()


