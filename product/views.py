from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer , categorySerializer


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class ProductDetail(APIView):
    def post(self, request):
        serializer = categorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class singleProduct(APIView):
    def get(self , request , pk):
        product = get_object_or_404(Product, pk=pk)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ProductSerializer(product)
            return Response(serializer.data , status=status.HTTP_200_OK)