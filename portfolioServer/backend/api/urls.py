from django.urls import path
from .views import ExampleView, ColorListCreateView

urlpatterns = [
    path('example/', ExampleView.as_view(), name='example'),
    path('colors/', ColorListCreateView.as_view(), name='color-list-create'),
]