from django.urls import path
from sport import views


app_name = 'sport'
urlpatterns = [
    path('page/<int:customer_pk>/', views.page_ini, name='page'),
    path('new-reservation/<int:customer_pk>/', views.new_customer_reservation, name='new-reservation'),
    path('add-new-reservation/', views.authorize_reservation, name='add-new-reservation'),
    path('show-reservation/<int:customer_pk>/', views.show_reservation, name='show-reservation'),
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete'),

]
