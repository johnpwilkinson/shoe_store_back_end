"""ShoeStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from api import views as api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'manufacturer', api_views.ManufacturerViewSet)
router.register(r'shoe_type', api_views.ShoeTypeViewSet)
router.register(r'shoe_color', api_views.ShoeColorViewSet)
router.register(r'shoe', api_views.ShoeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

#Joe will return to the African Savanna one day to locate, stalk, and extract 
#revenge on the owner of Jimmy Johns for poaching the animals that he grew up with