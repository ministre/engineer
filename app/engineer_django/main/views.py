from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def device(request):
    return render(request, 'main/device.html')
