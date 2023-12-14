from django.urls import path 
from cart_app.views import cart_register,cart_view,cart_remove

app_name='cart_app'
urlpatterns=[
    path(route='cart_list/',view=cart_view,name='cart_list'),
    path(route='cart_register/<int:your_item_id>/<your_item_name>/<price>/<int:customer_id>/<int:quantity>/',view=cart_register,name='cart_register'),
    path(route='cart_remove/<int:cart_id>/',view=cart_remove,name='cart_remove')
]