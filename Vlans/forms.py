from django.forms import ModelForm, TextInput
from django import forms
from .models import Vlan, IPaddress


class VlanForm(ModelForm):
    class Meta:
        model = Vlan
        fields = ['number','description']
        

class IPAddressForm(ModelForm):
    class Meta:
        model = IPaddress
        fields = ['ipaddress','description','used']
        widgets = {
        'ipaddress': TextInput(attrs={'class':'form-control','readonly':True}),
        }
    
