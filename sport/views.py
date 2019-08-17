from django.shortcuts import render
from sport.models import Field, Company, Reservation, Bill
from users.models import Customer
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def page_ini(request, customer_pk):
    context = {
        'customer': customer_pk,
    }
    return render(request, 'sport/page.html', context)


def new_customer_reservation(request, customer_pk):
    template = 'sport/reservation.html'
    context = {
        'customer': Customer.objects.get(pk=customer_pk),
        'fields': Field.objects.all(),
        'companies': Company.objects.all(),
    }

    return render(request, template, context)


def authorize_reservation(request):
    if request.method == 'POST':
        post_customer = Customer.objects.get(pk=request.POST['customer'])
        post_field = Field.objects.get(pk=request.POST['field'])
        post_company=Company.objects.get(pk=request.POST['company'])
        new_reservation=Reservation(
            schedule_date=request.POST['schedule_date'],
            schedule_time=request.POST['schedule_time'],
            customer_reserve=post_customer,
            field_reserve=post_field,
            company=post_company,
        )
        new_reservation.save()
        return HttpResponseRedirect(reverse('sport:page', kwargs={'customer_pk': request.POST['customer']}))
    return HttpResponse('No se puede guardar')


def show_reservation(request, customer_pk):
    template = 'sport/show_reservation.html'
    reservation_customer = Reservation.objects.filter(customer_reserve=customer_pk)

    paginator = Paginator(reservation_customer, 10)
    try:
        reservation = reservation_customer
    except PageNotAnInteger:
        reservation = reservation_customer
    except EmptyPage:
        reservation = reservation_customer

    return render(request, template, {'reservation': reservation}, {'paginator': paginator})


def delete_reservation(request, reservation_id):
    deleted_reservation = Reservation.objects.get(pk=reservation_id)
    deleted_reservation.delete()

    return HttpResponseRedirect(reverse('sport:show-reservation'))
