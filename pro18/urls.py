"""
URL configuration for pro18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from pro18.views import main_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('proapp18/',view=include('proapp18.urls'),name='proapp18'),
    path('crud_app/',view=include('crud_app.urls'),name='crud_app'),
    path('cart_app/',view=include('cart_app.urls'),name='cart_app'),
    path('buy_app/',view=include('buy_app.urls'),name='buy_app'),
    path('owner_app/',view=include('owner_app.urls'),name='owner_app'),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)