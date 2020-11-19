from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

class BidderSignUpView(CreateView):
    model = User
    form_class = BidderSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'bidder'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('bidders:list')