from rest_framework import viewsets,generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.generics import CreateAPIView,UpdateAPIView,DestroyAPIView

from rest_framework.permissions import AllowAny

# get all for both models.

class ProductViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# create for creating the models
class ProductCreateView(CreateAPIView):
    http_method_names = ["post"]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryCreateView(CreateAPIView):
    http_method_names = ["post"]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#Update the models
class ProductUpdateView(UpdateAPIView):
    http_method_names = ["put"]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class CategoryUpdateView(UpdateAPIView):
    http_method_names = ["put"]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
# Deleting the models
class ProductDeleteView(DestroyAPIView):
    http_method_names = ["delete"]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class CategoryDeleteView(DestroyAPIView):
    http_method_names = ["delete"]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
#Get but with params
