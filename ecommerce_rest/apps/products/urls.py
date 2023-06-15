from django.urls import path
from apps.products.api.views.views import MeasureUnitListAPIView

urlpatterns = [
    path('measure-unit/', MeasureUnitListAPIView.as_view(), name='measure-unit-list'),
]