from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Device


class GetPasswordForm(ModelForm):
    sn = forms.CharField(required=False, label=_('Serial Number'), min_length=5, max_length=30)

    class Meta:
        model = Device
        labels = {
            'vendor': _('Vendor'),
            'model': _('Model'),
        }
        fields = '__all__'
