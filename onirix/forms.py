from django.forms import ModelForm
from onirix.models import Newsletter

class NewsletterForm(ModelForm):
    
    class Meta:
        model= Newsletter
        fields = ['email', ]
        labels = {
            "email": ""
            }
