from django.urls import path
from owner_app.views import owner_register_view,otp_view,change_pass_view,sample_home_view,owner_login_view,sub_login_view
app_name='owner_app'

urlpatterns=[
    path(route='owner_register/',view=owner_register_view,name='owner_register'),
    path(route='otp_view/<int:pk>/',view=otp_view,name='otp_view'),
    path(route='change_pass_view/<int:pk>/',view=change_pass_view,name='change_pass_view'),
    path(route='sample_home_view/',view=sample_home_view,name='sample_home_view'),
    path(route='owner_login_view/<int:pk>/',view=owner_login_view,name='owner_login_view'),
    path(route='sub_login_view/<int:pk>/',view=sub_login_view,name='sub_login_view'),
]
