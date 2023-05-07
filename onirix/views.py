from django.shortcuts import render
from django.views.generic.edit import CreateView
from onirix.models import Contact_US, Newsletter, Payments
from django.contrib.messages.views import SuccessMessageMixin
from onirix.forms import NewsletterForm

# Create your views here.




class IndexView(SuccessMessageMixin, CreateView):
    form_class = NewsletterForm
    template_name = 'onirix/index.html'
    success_message = 'You are Suscribed'
    success_url = '/'
    

def pricing_view(request):
    template_name='onirix/pricing.html'
    return render(request, template_name)

class Contact_us(SuccessMessageMixin,CreateView):
    template_name = 'onirix/contact.html'
    model = Contact_US
    fields = ['name', 'email', 'message']
    success_message = "We will Contact Your Accordingly, Thank You!!!"
    success_url = '/'


class PaymentsView(SuccessMessageMixin,CreateView):
    template_name = 'onirix/payments.html'
    model = Payments
    fields = ['name', 'email', 'price']
    success_message = "We will contact you for the Payment, Thank You for your Interest!!!"
    success_url = '/'


def health_view(request):
    template_name = 'onirix/health.html'
    return render(request, template_name)