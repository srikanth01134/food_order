from django.urls import path
from crud_app.views import catagory_view,display,updates,deletes,items_view,item_update,items_list,item_delete,details_view
app_name='crud_app'

urlpatterns=[
    #========FOR CATEGORY CREATED BY THE HOTEL_REGISTER======
    path(route='catagory/',view=catagory_view,name='catagory'),
    path(route='display/',view=display,name='display'),
    path(route='updates/<int:pk>/',view=updates,name='updates'),
    path(route='deletes/<int:pk>/',view=deletes,name='deletes'),
    #========FOR ITEMS CREATED ==============================
     path(route='items/',view=items_view,name='items'),
    path(route='items_list/',view=items_list,name='items_list'),
    path(route='item_update/<int:pk>/',view=item_update,name='item_update'),
    path(route='item_delete/<int:pk>/',view=item_delete,name='item_delete'),
    path(route='details_view/<pk>/',view=details_view,name='details_view'),
    # path(route='item_details_view/<pk>/',view=item_details_view,name='item_details_view'),
]