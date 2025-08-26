from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.mail import mail_admins
from django.contrib import messages
from django.utils.html import strip_tags
from django.views.generic import FormView, TemplateView

from .forms import ContactForm
from .models import ContactMessage

class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('pages:contact')

    def get_initial(self):
        initial = super().get_initial()
        u=self.request.user
        if u.is_authenticated and getattr(u, 'email', None):
            initial['name'] = getattr(u, 'get_full_name', lambda: u.username)()
            initial['email'] = u.email
        return initial

     
        
    # not finished!!