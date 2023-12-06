from django.urls import path
from proapp18.views import customer_register,login_view,home_view,logout_view,otp_view
app_name = 'proapp18'

urlpatterns = [
    path(route='',view=customer_register,name='register'),
    path(route='login/',view=login_view,name='login'),
    path(route='home/',view=home_view, name='home'),
    path(route='logout/',view=logout_view,name='logout'),
    path(route='otp_confirm/',view=otp_view,name='otp')
]
