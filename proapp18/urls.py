from django.urls import path
from proapp18.views import customer_register,login_view,home_view,logout_view,otp_view,start_view,home_view,category_user_view,items_user_view
app_name = 'proapp18'

urlpatterns = [
    path(route='',view=start_view,name='start'),
    path(route='register/',view=customer_register,name='register'),
    path(route='login/',view=login_view,name='login'),
    path(route='otp/',view=otp_view,name='otp'),
    path(route='home/',view=home_view, name='home'),
    path(route='logout/',view=logout_view,name='logout'),
    path(route='hotel1/',view=home_view,name='hotel'),
    path(route='category_user/<int:pk>/',view=category_user_view,name='category_user'),
    path(route='items_user/<int:hotel>/<int:category>/',view=items_user_view,name='items_user'),
  
]
