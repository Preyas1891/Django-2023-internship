import django.forms as form
from.models import bureaucrat

class bureaucratform(form.ModelForm):
    class Meta:
        model = bureaucrat
        fields= '__all__'
