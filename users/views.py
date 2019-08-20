from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse
from users.models import Customer

# Create your views here.


def login_customer(request):
    if request.method == 'POST':
        try:
            customer = Customer.objects.get(email=request.POST['email'], password=request.POST['password'])
        except Customer.DoesNotExist:
            return HttpResponse('User does not exist!!!')

        return HttpResponseRedirect(reverse('sport:page', kwargs={'customer_pk': customer.pk}))
    elif request.method == 'GET':
        template = 'users/login.html'
        return render(request, template)
    return HttpResponse('Error, Method not allowed!')


def register_customer(request):
    if request.method == 'POST':
        new_customer = Customer(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            address=request.POST['address'],
            password=request.POST['password'],
        )
        new_customer.save()
        return HttpResponseRedirect(reverse('users:login'))
    elif request.method == 'GET':
        template = 'users/register.html'
        return render(request, template)
    return HttpResponse('Error: No se puede Guardar!')