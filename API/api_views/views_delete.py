from rest_framework.generics import DestroyAPIView
from ..models import Product, Category
from ..serializers import ProductSerializer, CategorySerializer


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