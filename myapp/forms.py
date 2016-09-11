from django.forms import ModelForm, Form, ModelChoiceField

from .models import Bid

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['date', 'manager', 'bid_partner', 'bid_type', 'bid_status', 'bid_product', 'amount']

class BidEditForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['date', 'manager', 'bid_partner', 'bid_type', 'bid_status', 'bid_product', 'amount']

class StatusForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['bid_status',]
