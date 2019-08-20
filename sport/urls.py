from django.urls import path
from sport import views


app_name = 'sport'
urlpatterns = [
    path('page/<int:customer_pk>/', views.page_ini, name='page'),
    path('new-reservation/<int:customer_pk>/', views.create_reservation, name='new-reservation'),
    path('show-reservation/<int:customer_pk>/', views.show_reservation, name='show-reservation'),
    path('edit-reservation/<int:reservation_pk>/', views.edit_reservation, name='edit-reservation'),
    path('save-reservation/<int:reservation_pk>/', views.confirm_edit_reservation, name='save-reservation'),
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete'),
    path('new-field/', views.create_field, name='new-field'),
    path('edit-field/<int:field_pk>/', views.edit_field, name='edit-field'),
    path('delete-field/<int:field_pk>/', views.delete_field, name='delete-field'),
    path('show-field/', views.show_field, name='show-field'),
    path('new-company/', views.create_company, name='new-company'),
    path('show-company/', views.show_company, name='show-company'),
    path('edit-company/<int:company_pk>/', views.edit_company, name='edit-company'),
    path('delete-company/<int:company_pk>/', views.delete_company, name='delete-company'),
    path('profile/<int:customer_pk>/', views.profile, name='profile'),
    path('edit-profile/<int:customer_pk>/', views.edit_profile, name='edit-profile'),
]
