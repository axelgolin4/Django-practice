from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

# Create your models here.


class MeasureUnit(BaseModel):

    description = models.CharField("Descripción", max_length=50, null=False, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    
    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return self.description
    

class CategoryProduct(BaseModel):

    description = models.CharField("Descripción", max_length=50, null=False, blank=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name="Unidad de Medida")
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'

    def __str__(self):
        return self.description

class Indicador(BaseModel):

    descount_value = models.PositiveSmallIntegerField(default=0)
    categoryProduct = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name="Categoría de Producto")
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Indicador de oferta'
        verbose_name_plural = 'Indicadores de ofertas'

    def __str__(self):
        return f'Oferta de la categoria {self.categoryProduct} : {self.descount_value}%'
    
class Product(BaseModel):
    name = models.CharField("Nombre", max_length=150, null=False, blank=False, unique=True)
    description = models.TextField("Descripción", null=False, blank=False)
    image = models.ImageField("Imagen", upload_to='products/', null=True, blank=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.name


