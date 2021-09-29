from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import GetPasswordForm
from .models import Model
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from .gen import dynamic_pass


@login_required
def device(request):
    form = GetPasswordForm()
    if request.method == 'POST':
        get_password_form = GetPasswordForm(request.POST)
        if get_password_form.is_valid():
            message = get_password(model_id=request.POST['model'], sn=request.POST['sn'])
            return render(request, 'main/device.html', {'message': message, 'form': form})
        return render(request, 'main/device.html', {'message': [False, _('Unknown Error')], 'form': form})
    else:
        return render(request, 'main/device.html', {'form': form})


def get_password(model_id: int, sn: str):
    model = get_object_or_404(Model, id=model_id)
    password_type = model.password_type
    if password_type == 0:
        # static
        if model.password:
            return [True, model.password]
        else:
            return [False, _('Static password not specified')]
    elif password_type == 1:
        # static + last 5 characters of sn
        if sn:
            if model.password:
                return [True, model.password + sn]
            else:
                return [False, _('Static password not specified')]
        else:
            return [False, _('Serial number not specified')]
    else:
        # dynamic
        return 'dynamic'
