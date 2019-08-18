from django.urls import path
from sport import views


app_name = 'sport'
urlpatterns = [
    path('page/<int:customer_pk>/', views.page_ini, name='page'),
    path('new-reservation/<int:customer_pk>/', views.new_customer_reservation, name='new-reservation'),
    path('add-new-reservation/', views.authorize_reservation, name='add-new-reservation'),
    path('show-reservation/<int:customer_pk>/', views.show_reservation, name='show-reservation'),
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete'),
    path('new-field/', views.create_field, name='new-field'),
    path('add-new-field/', views.authorize_new_field, name='add-new-field'),
    path('edit-field/<int:field_pk>/', views.edit_field, name='edit-field'),
    path('save-field/<int:field_pk>/', views.confirm_edit_field, name='save-field'),
    path('delete-field/<int:field_pk>/', views.delete_field, name='delete-field'),
    path('show-field/', views.show_field, name='show-field'),
    path('new-company/', views.create_company, name='new-company'),
    path('add-new-company/', views.authorize_new_company, name='add-new-company'),
    path('show-company/', views.show_company, name='show-company'),
    path('edit-reservation/<int:reservation_pk>/', views.edit_reservation, name='edit-reservation'),
    path('save-reservation/<int:reservation_pk>/', views.confirm_edit_reservation, name='save-reservation'),
    path('profile/<int:customer_pk>/', views.profile, name='profile'),
    path('edit-profile/<int:customer_pk>/', views.edit_profile, name='edit-profile'),
    path('save-profile/<int:customer_pk>/', views.confirm_edit_profile, name='save-profile'),
    path('edit-company/<int:company_pk>/', views.edit_company, name='edit-company'),
    path('save-company/<int:company_pk>/', views.confirm_edit_company, name='save-company'),
    path('delete-company/<int:company_pk>/', views.delete_company, name='delete-company'),
]
