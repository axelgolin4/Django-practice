from django.urls import path
from apps.users.views import user_view, user_detail_view


urlpatterns = [
    path('usuario/', user_view, name = 'usuario_view'),
    path('usuario/<int:pk>', user_detail_view, name = 'usuario_datail_view')
]