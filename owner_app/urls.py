from django.urls import path
from owner_app.views import owner_register_view,login_view,otp_view
app_name='owner_app'

urlpatterns=[
    path(route='owner_register/',view=owner_register_view,name='owner_register'),
    path(route='owner_login/',view=login_view,name='owner_login'),
    path(route='otp_view/',view=otp_view,name='otp_view'),
]