from rest_framework.generics import UpdateAPIView
from ..models import Product, Category
from ..serializers import ProductSerializer, CategorySerializer

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