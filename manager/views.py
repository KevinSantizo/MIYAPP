from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse
from manager.models import Manager
from sport.models import Company
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

    paginator = Paginator(list_company, 10)
    try:
        company_list = list_company
    except PageNotAnInteger:
        company_list = list_company
    except EmptyPage:
        company_list = list_company

    return render(request, template, {'company_list': company_list,  'manager_pk': manager_pk}, {'paginator': paginator})


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
            'company': Company.objects.get(pk=company_pk)
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def delete_company(request, company_pk):
    deleted_company = Company.objects.get(id=company_pk)
    deleted_company.delete()

    return HttpResponseRedirect(reverse('manager:show-company',  kwargs={'manager_pk': company_pk}))