from django.urls import path
from manager import views

app_name = 'manager'
urlpatterns = [
    path('page-manager/<int:manager_pk>/', views.page_manager, name='page-manager'),
    path('login/', views.login_manager, name='login'),
    path('register/', views.register_manager, name='register'),
    path('new-company/<int:manager_pk>/', views.create_company, name='new-company'),
    path('show-company/<int:manager_pk>/', views.show_company, name='show-company'),
    path('edit-company/<int:company_pk>/', views.edit_company, name='edit-company'),
    path('delete-company/<int:company_pk>/', views.delete_company, name='delete-company'),
    path('show-championship/<int:manager_pk>/', views.show_championship, name='show-championship'),
    path('new-championship/<int:manager_pk>/', views.create_championship, name='new-championship'),
    path('edit-championship/<int:championship_pk>/', views.edit_championship, name='edit-championship'),
]