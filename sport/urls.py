from django.urls import path
from sport import views


app_name = 'sport'
urlpatterns = [
    path('page/<int:customer_pk>/', views.page_ini, name='page'),
    path('new-reservation/<int:customer_pk>/', views.create_reservation, name='new-reservation'),
    path('show-reservation/<int:customer_pk>/', views.show_reservation, name='show-reservation'),
    path('save-reservation/<int:reservation_pk>/', views.edit_reservation, name='save-reservation'),
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete'),
    path('new-field/', views.create_field, name='new-field'),
    path('edit-field/<int:field_pk>/', views.edit_field, name='edit-field'),
    path('delete-field/<int:field_pk>/', views.delete_field, name='delete-field'),
    path('show-field/', views.show_field, name='show-field'),
    path('profile/<int:customer_pk>/', views.profile, name='profile'),
    path('edit-profile/<int:customer_pk>/', views.edit_profile, name='edit-profile'),
    path('show-championship/<int:customer_pk>/', views.show_championship, name='show-championship'),
    path('registration/<int:customer_pk>/', views.register_team, name='registration'),
]
