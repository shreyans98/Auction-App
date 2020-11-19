from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Vendor(models.Model):
    #user_rec = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    bid = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.title



class Bidder(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    content = models.TextField()

    def __unicode__(self):
        return self.name



class vendorProfile(models.Model):
    vendor = models.OneToOneField(User,on_delete=models.CASCADE,related_name="Profile")
    description = models.TextField(blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    date_bid = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor.username



class bidderProfile(models.Model):
    bidder = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profiles")
    description = models.TextField(blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    date_bid = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bidder.username



