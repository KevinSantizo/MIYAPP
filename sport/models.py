from django.db import models
from users.models import Customer
from django.utils import timezone
from django.urls import reverse
import uuid


# Create your models here.


class Field(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
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

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('sport:page', args=[str(self.pk)])


class Bill(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    token = models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')


