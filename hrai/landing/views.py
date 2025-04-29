from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import CandidateSignUpForm
from .models import Profile

class RegisterView(FormView):
    template_name = 'landing/register.html'
    form_class = CandidateSignUpForm
    success_url = reverse_lazy('connection')

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user, phone=form.cleaned_data['phone'])
        return super().form_valid(form)



class ConnectionView(TemplateView):
    template_name = 'landing/connection.html'


class ConnectionView(TemplateView):
    template_name = 'landing/connection.html'