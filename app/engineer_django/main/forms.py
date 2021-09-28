from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Device


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        labels = {
            'vendor': _('Vendor'),
            'model': _('Model'),
            'sn': _('Serial Number'),
        }
        fields = '__all__'
