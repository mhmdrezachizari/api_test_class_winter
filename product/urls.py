from django.urls import include , path
from django.contrib import admin
from .views import ProductList ,ProductDetail
urlpatterns = [
    path('' , ProductList.as_view()),
    path('detail/', ProductDetail.as_view()),


]
