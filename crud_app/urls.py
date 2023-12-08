from django.urls import path
from crud_app.views import catagory_view,display,updates,deletes,veg
app_name='crud_app'

urlpatterns=[
    path(route='category/',view=catagory_view,name='catagory_view'),
    path(route='display/',view=display,name='display'),
    path(route='updates/<int:pk>/',view=updates,name='updates'),
    path(route='deletes/<int:pk>/',view=deletes,name='deletes'),
    path(route='veg/',view=veg,name='veg'),
]