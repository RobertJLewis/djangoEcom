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

     
    def form_valid(self, form):
        msg: ContactMessage = form.save(commit=False)
        if self.request.user.is_authenticated:
            msg.user = self.request.user
        msg.ip_address = self.request.META.get('REMOTE_ADDR')
        msg.save() 

        subject = f"Contact form: {msg.name} <{msg.email}>" 
        body = strip_tags(msg.enquiry)

        mail_admins(subject, body, fail_silently=True)
        messages.success(self.request, "Thanks! We have recieved your message")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Please fix the errors below and resubmit")
        return super().form_invalid(form)

class ContactThanksView(TemplateView):
    template_name = 'pages/contact_thanks.html'