from django.urls import path 
from cart_app.views import cart_register,cart_view,cart_remove

app_name='cart_app'
urlpatterns=[
    path(route='cart_list/<int:pk>/',view=cart_view,name='cart_list'),
    path(route='cart_register/',view=cart_register,name='cart_register'),
    path(route='cart_remove/<int:cart_id>/<int:hotel_id>/',view=cart_remove,name='cart_remove')
]