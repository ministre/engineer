from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DeviceForm


@login_required
def device(request):
    return render(request, 'main/device.html', {
        'form': DeviceForm()
    })
