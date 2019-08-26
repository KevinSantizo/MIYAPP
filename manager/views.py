from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse
from manager.models import Manager
from sport.models import Company, Championship, Field
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def page_manager(request, manager_pk):
    template = 'manager/page.html'
    context = {
        'manager': manager_pk,
    }

    return render(request, template, context)


def login_manager(request):
    if request.method == 'POST':
        try:
            manager = Manager.objects.get(email=request.POST['email'], password=request.POST['password'])
        except Manager.DoesNotExist:
            return HttpResponse('User does not exist!!!')

        return HttpResponseRedirect(reverse('manager:page-manager', kwargs={'manager_pk': manager.pk}))
    elif request.method == 'GET':
        template = 'manager/login.html'
        return render(request, template)
    return HttpResponse('Error, Method not allowed!')


def register_manager(request):
    if request.method == 'POST':
        new_manager = Manager(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            address=request.POST['address'],
            password=request.POST['password'],
        )
        new_manager.save()
        return HttpResponseRedirect(reverse('manager:login'))
    elif request.method == 'GET':
        template = 'manager/register.html'
        return render(request, template)
    return HttpResponse('Error: No se puede Guardar!')


def create_company(request, manager_pk):
    if request.method == 'POST':
        new_company = Company(
            name=request.POST['name'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            email=request.POST['email'],
        )
        new_company.save()
        return HttpResponseRedirect(reverse('manager:show-company', kwargs={'manager_pk': manager_pk}))
    elif request.method == 'GET':
        template = 'manager/create_company.html'
        return render(request, template, {'manager_pk': manager_pk})
    return HttpResponse('No se puede guardar')


def show_company(request, manager_pk):
    template = 'manager/show_company.html'
    list_company = Company.objects.all()
    num_companies = Company.objects.all().count()
    paginator = Paginator(list_company, 10)
    try:
        company_list = list_company
    except PageNotAnInteger:
        company_list = list_company
    except EmptyPage:
        company_list = list_company

    return render(request, template, {'company_list': company_list, 'companies': num_companies, 'manager_pk': manager_pk}, {'paginator': paginator})


def edit_company(request, company_pk):
    if request.method == 'POST':
        updated_company = Company.objects.get(pk=company_pk)
        updated_company.name = request.POST['name']
        updated_company.address = request.POST['address']
        updated_company.phone = request.POST['phone']
        updated_company.email = request.POST['email']
        updated_company.save()

        return HttpResponseRedirect(reverse('manager:show-company', kwargs={'manager_pk': company_pk}))
    elif request.method == 'GET':
        template = 'manager/edit_company.html'
        context = {
            'company': Company.objects.get(pk=company_pk),
            'manager': company_pk,
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def delete_company(request, company_pk):
    deleted_company = Company.objects.get(id=company_pk)
    deleted_company.delete()

    return HttpResponseRedirect(reverse('manager:show-company',  kwargs={'manager_pk': company_pk}))


def show_championship(request, manager_pk):
    template = 'manager/show_championship.html'
    context = {
        'manager_pk': manager_pk,
        'champ': Championship.objects.all(),
        'championships': Championship.objects.all().count(),
    }
    return render(request, template, context)


def create_championship(request, manager_pk):
    if request.method == 'POST':
        post_company = Company.objects.get(pk=request.POST['championship_company'])
        new_championship = Championship(
            championship_company=post_company,
            name_championship=request.POST['name_championship'],
            description=request.POST['description'],
            registration_price=request.POST['registration_price'],
        )
        new_championship.save()
        return HttpResponseRedirect(reverse('manager:show-championship', kwargs={'manager_pk': manager_pk}))
    elif request.method == 'GET':
        template = 'manager/create_championship.html'
        companies = Company.objects.all()
        return render(request, template, {'companies': companies, 'manager_pk': manager_pk})
    return HttpResponse('No se puede guardar')


def edit_championship(request, championship_pk):
    if request.method == 'POST':
        post_company = Company.objects.get(pk=request.POST['championship_company'])
        update_championship = Championship.objects.get(pk=championship_pk)
        update_championship.championship_company = post_company
        update_championship.name_championship = request.POST['name_championship']
        update_championship.description = request.POST['description']
        update_championship.registration_price = request.POST['registration_price']
        update_championship.save()

        return HttpResponseRedirect(reverse('manager:show-championship', kwargs={'manager_pk': championship_pk}))
    elif request.method == 'GET':
        template = 'manager/edit_championship.html'
        company_champ = Championship.objects.get(pk=championship_pk)
        context = {
            'championship': Championship.objects.get(pk=championship_pk),
            'companies': Company.objects.all(),
            'company_instance': company_champ,
            'manager_pk': championship_pk,

        }
        return render(request, template, context)
    return HttpResponse('No se puede guardar')


def create_field(request):
    if request.method == 'POST':
        post_company = Company.objects.get(pk=request.POST['company'])
        new_field = Field(
            company=post_company,
            name=request.POST['name'],
            status=request.POST['status'],
            type=request.POST['type'],
            price=request.POST['price'],
        )
        new_field.save()
        return HttpResponseRedirect(reverse('manager:show-field'))
    elif request.method == 'GET':
        template = 'manager/new_field.html'
        context = {
            'companies': Company.objects.all(),
        }
        return render(request, template, context)
    return HttpResponse('No se puede guardar')


def show_field(request):
    template = 'sport/show_field.html'
    list_field = Field.objects.all()

    paginator = Paginator(list_field, 10)
    try:
        field_list = list_field
    except PageNotAnInteger:
        field_list = list_field
    except EmptyPage:
        field_list = list_field

    return render(request, template, {'field_list': field_list}, {'paginator': paginator})


def edit_field(request, field_pk):
    if request.method == 'POST':
        updated_field = Field.objects.get(pk=field_pk)
        updated_field.status = request.POST['status']
        updated_field.type = request.POST['type']
        updated_field.price = request.POST['price']
        updated_field.save()

        return HttpResponseRedirect(reverse('sport:show-field'))
    elif request.method == 'GET':
        template = 'manager/edit_field.html'
        context = {
            'field': Field.objects.get(pk=field_pk)
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def delete_field(request, field_pk):
    deleted_field = Field.objects.get(id=field_pk)
    deleted_field.delete()

    return HttpResponseRedirect(reverse('manager:show-field'))