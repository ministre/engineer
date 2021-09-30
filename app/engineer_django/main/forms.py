from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Device, Model


class GetPasswordForm(ModelForm):
    sn = forms.CharField(required=False, label=_('Serial Number'), min_length=5, max_length=30)

    class Meta:
        model = Device
        labels = {
            'vendor': _('Vendor'),
            'model': _('Model'),
        }
        fields = '__all__'


class DevForm(ModelForm):
    class Meta:
        model = Model
        labels = {
            'vendor': _('Vendor'),
            'name': _('Model Name'),
            'password_type': _('Password Type'),
            'password': _('Password'),
        }
        fields = '__all__'
        PASS_TYPE = (
            ('0', _('Static')),
            ('1', _('Static + last 5 characters of serial number')),
            ('3', _('Hash')),
        )
        widgets = {'password_type': forms.Select(choices=PASS_TYPE, attrs={'class': 'form-control'})}
