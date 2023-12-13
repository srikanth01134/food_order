from django.urls import path
from proapp18.views import customer_register,login_view,home_view,logout_view,otp_view,start_view,hotel1_view,hotel_view,hotel_display,hotel_update,hotel_delete
app_name = 'proapp18'

urlpatterns = [
    path(route='',view=start_view,name='start'),
    path(route='register/',view=customer_register,name='register'),
    path(route='login/',view=login_view,name='login'),
    path(route='otp/',view=otp_view,name='otp'),
    path(route='home/',view=home_view, name='home'),
    path(route='logout/',view=logout_view,name='logout'),
    path(route='hotel1/',view=hotel1_view,name='hotel'),
    path(route='hotel_register/',view=hotel_view,name='hotel_register'),
    path(route='hotel_display/',view=hotel_display,name='hotel_display'),
    path(route='hotel_update/<int:pk>/',view=hotel_update,name='hotel_update'),
    path(route='hotel_delete/<int:pk>/',view=hotel_delete,name='hotel_delete'),
]
