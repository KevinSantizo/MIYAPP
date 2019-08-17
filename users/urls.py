from django.urls import path
from users import views


app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('auth/', views.authorize_login, name='auth'),
    path('register/', views.register, name='register'),
    path('save-customer/', views.save_register_customer, name='save-customer'),
]