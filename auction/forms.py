from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from auction.models import Vendor, Bidder, User

class VendorSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        vendor = Vendor.objects.create(user=user)
        vendor.interests.add(*self.cleaned_data.get('interests'))
        return user


class BidderSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_bidder = True
        if commit:
            user.save()

        return user

                        