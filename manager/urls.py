from django.urls import path
from manager import views

app_name = 'manager'
urlpatterns = [
    path('page-manager/<int:manager_pk>/', views.page_manager, name='page-manager'),
    path('login/', views.login_manager, name='login'),
    path('register/', views.register_manager, name='register')
]