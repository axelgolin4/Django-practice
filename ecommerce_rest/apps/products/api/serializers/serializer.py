from apps.products.models import MeasureUnit, CategoryProduct, Indicador

from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        exclude = ('state',)
    

class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        exclude = ('state',)

class IndicadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicador
        exclude = ('state',)
