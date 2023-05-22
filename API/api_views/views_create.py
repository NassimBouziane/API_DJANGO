from rest_framework.generics import CreateAPIView
from ..models import Product, Category
from ..serializers import ProductSerializer, CategorySerializer

class ProductCreateView(CreateAPIView):
    http_method_names = ["post"]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryCreateView(CreateAPIView):
    http_method_names = ["post"]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
