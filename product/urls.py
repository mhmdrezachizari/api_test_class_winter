from django.urls import include , path
from django.contrib import admin
from .views import ProductList, ProductDetail, singleProduct

urlpatterns = [
    path('' , ProductList.as_view()),
    path('detail/', ProductDetail.as_view()),

    path('single/<int:pk>' , singleProduct.as_view()),


]
