from django.urls import path
from .views import ProductoListView

app_name="catalogo"
urlpatterns=[
    path('', ProductoListView.as_view(),name='lista')
]