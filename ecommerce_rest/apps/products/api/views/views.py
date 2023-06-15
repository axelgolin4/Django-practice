from rest_framework import generics

from apps.products.models import MeasureUnit
from apps.products.api.serializers.serializer import MeasureUnitSerializer

class MeasureUnitListAPIView(generics.ListAPIView):
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return MeasureUnit.objects.filter(state=True)
    
    
