from rest_framework import generics
from ..models import Product, Category
from ..serializers import ProductSerializer, CategorySerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer