from django.shortcuts import render
from sport.models import Field, Company, Reservation, Bill, AssignGroup, Championship, Team
from users.models import Customer
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def page_ini(request, customer_pk):
    template = 'sport/page.html',
    context = {
        'customer': customer_pk,
    }
    return render(request,  template, context)


def create_reservation(request, customer_pk):
    if request.method == 'POST':
        post_customer = Customer.objects.get(pk=request.POST['customer'])
        post_field = Field.objects.get(pk=request.POST['field'])
        post_company = Company.objects.get(pk=request.POST['company'])
        new_reservation_customer=Reservation(
            schedule_date=request.POST['schedule_date'],
            schedule_time=request.POST['schedule_time'],
            customer_reserve=post_customer,
            field_reserve=post_field,
            company_reserve=post_company,
        )
        new_reservation_customer.save()
        return HttpResponseRedirect(reverse('sport:show-reservation', kwargs={'customer_pk': request.POST['customer']}))
    elif request.method == 'GET':
        template = 'sport/reservation.html'
        context = {
            'customer': Customer.objects.get(pk=customer_pk),
            'fields': Field.objects.all(),
            'companies': Company.objects.all(),
        }
        return render(request, template, context)
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

    return render(request, template, {'reservation': reservation, 'customer_pk': customer_pk}, {'paginator': paginator}) # FALTABA AGREGAR EL CUSTOMERPK POR ALGUNA RAZON NO IBA DENTRO DEL RESERVATION


def edit_reservation(request, reservation_pk):
    if request.method == 'POST':
        post_company = Company.objects.get(pk=request.POST['company'])
        post_field = Field.objects.get(pk=request.POST['field'])
        updated_reservation = Reservation.objects.get(pk=reservation_pk)
        updated_reservation.schedule_date = request.POST['schedule_date']
        updated_reservation.schedule_time = request.POST['schedule_time']
        updated_reservation.company_reserve = post_company
        updated_reservation.field_reserve = post_field
        updated_reservation.save()

        return HttpResponseRedirect(reverse('sport:show-reservation', kwargs={'customer_pk': updated_reservation.customer_reserve.id}))
    elif request.method == 'GET':
        template = 'sport/edit_reservation.html'
        company_reserve = Reservation.objects.get(pk=reservation_pk)
        field_reserve = Reservation.objects.get(pk=reservation_pk)
        context = {
            'reservation': Reservation.objects.get(pk=reservation_pk),
            'companies': Company.objects.all(),
            'fields': Field.objects.all(),
            'company_instance': company_reserve,
            'field_instance': field_reserve,
        }

        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def delete_reservation(request, reservation_id):
    deleted_reservation = Reservation.objects.get(id=reservation_id)
    deleted_reservation.delete()

    return HttpResponseRedirect(reverse('sport:show-reservation',  kwargs={'customer_pk': deleted_reservation.customer_reserve.id}))


def profile(request, customer_pk):
    template = 'sport/profile.html'
    context = {
        'customer': Customer.objects.get(pk=customer_pk),
        'reservation': Reservation.objects.filter(customer_reserve=customer_pk).count(),
        'field': Field.objects.all(),
    }
    return render(request, template, context)


def edit_profile(request, customer_pk):
    if request.method == 'POST':
        updated_profile = Customer.objects.get(pk=customer_pk)
        updated_profile.first_name = request.POST['first_name']
        updated_profile.last_name = request.POST['last_name']
        updated_profile.phone = request.POST['phone']
        updated_profile.email = request.POST['email']
        updated_profile.address = request.POST['address']
        updated_profile.password = request.POST['password']
        updated_profile.save()
        return HttpResponseRedirect(reverse('sport:profile',  kwargs={'customer_pk': customer_pk}))
    elif request.method == 'GET':
        template = 'sport/edit_profile.html'
        context = {
            'customer': Customer.objects.get(pk=customer_pk)
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def show_championship(request, customer_pk):
    template = 'sport/show_championship.html'
    context = {
        'championships': Championship.objects.all(),
        'customer_pk': customer_pk,
    }

    return render(request, template, context)


def register_team(request, customer_pk):
    if request.method == 'POST':
        post_customer = Customer.objects.get(pk=request.POST['agent_team'])
        new_team = Team(
            agent_team=post_customer,
            name_team=request.POST['name_team'],
            players=request.POST['players'],
        )
        new_team.save()
        return HttpResponseRedirect(reverse('sport:show-championship', kwargs={'customer_pk': request.POST['agent_team']}))
    elif request.method == 'GET':
        template = 'sport/registration.html'
        context = {
            'customer': Customer.objects.get(pk=customer_pk),
            'team_agent': Team.objects.filter(agent_team=customer_pk)

        }
        return render(request, template, context)
    return HttpResponse('No se puede guardar')


