from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import GetPasswordForm, DevForm
from .models import Model
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .gen import dynamic_pass


@login_required
def device(request):
    form = GetPasswordForm()
    if request.method == 'POST':
        get_password_form = GetPasswordForm(request.POST)
        if get_password_form.is_valid():
            message = get_password(model_id=request.POST['model'], sn=request.POST['sn'])
            return render(request, 'main/get_pass.html', {'message': message, 'form': form})
        return render(request, 'main/get_pass.html', {'message': [False, _('Unknown Error')], 'form': form})
    else:
        return render(request, 'main/get_pass.html', {'form': form})


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
                return [True, model.password + sn[-5:]]
            else:
                return [False, _('Static password not specified')]
        else:
            return [False, _('Serial number not specified')]
    else:
        # sn & vendor hash
        if sn:
            pwd = dynamic_pass(manufacturer=model.vendor.name, sn=sn)
            return [True, pwd]
        else:
            return [False, _('Serial number not specified')]


@method_decorator(login_required, name='dispatch')
class ModelListView(ListView):
    context_object_name = 'models'
    queryset = Model.objects.all().order_by('name')
    template_name = 'main/models.html'


@method_decorator(login_required, name='dispatch')
class ModelCreate(CreateView):
    model = Model
    form_class = DevForm
    template_name = 'main/model_create.html'

    def get_success_url(self):
        return reverse('models')


@method_decorator(login_required, name='dispatch')
class ModelUpdate(UpdateView):
    model = Model
    form_class = DevForm
    template_name = 'main/model_update.html'

    def get_success_url(self):
        return reverse('models')


@method_decorator(login_required, name='dispatch')
class ModelDelete(DeleteView):
    model = Model
    template_name = 'main/model_delete.html'

    def get_success_url(self):
        return reverse('models')
