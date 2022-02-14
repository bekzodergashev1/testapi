from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('products/', all_products, name='products'),
    path('product/detail/<int:pk>', product_detail),
]