"""MyProject URL Configuration

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
from django.urls import path, include, URLPattern  
from auction import views

from rest_framework.routers import DefaultRouter
from .views import vendorProfileListCreateView, vendorProfileDetailView
from .models import vendorProfile, bidderProfile
admin.autodiscover()

#from marketing.views import HomePage

urlpatterns = [
    path(r'(?P<pk>\d+)/$', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('auction.urls', namespace='auction')),
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("api/auction/", include("auction.urls")),


    path("all-profiles", vendorProfileListCreateView.as_view(), name="all-profiles")
    path("profile/<int:pk>", vendorProfileDetailView.as_view(), name="profile")
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/vendor/', vendor.VendorSignUpView.as_view(), name='vendor_signup'),
    path('accounts/signup/bidder/', bidder.BidderSignUpView.as_view(), name='bidder_signup'),


]
