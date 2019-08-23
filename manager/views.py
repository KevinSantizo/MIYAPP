from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse
from manager.models import Manager

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