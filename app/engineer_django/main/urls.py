from django.urls import path
from . import views


urlpatterns = [
    path('', views.device, name='main'),
    path('models', views.ModelListView.as_view(), name='models'),
    path('model_create', views.ModelCreate.as_view(), name='model_create'),
    path('model_update/<int:pk>/', views.ModelUpdate.as_view(), name='model_update'),
    path('model_delete/<int:pk>/', views.ModelDelete.as_view(), name='model_delete'),
]
