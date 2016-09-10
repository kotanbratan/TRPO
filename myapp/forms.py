from django.forms import ModelForm, Form

from myapp.models import Status

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['status_name',]
