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



class AvailableProductListView(generics.ListAPIView):
    http_method_names = ["get"]
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(quantity__gt=0)

        category = self.request.query_params.get('category', None)
        brand = self.request.query_params.get('brand', None)
        size = self.request.query_params.get('size', None)
        quantity = self.request.query_params.get('quantity', None)
        status = self.request.query_params.get('status', None)

        if category:
            queryset = queryset.filter(category=category)
        if brand:
            queryset = queryset.filter(brand=brand)
        if size:
            queryset = queryset.filter(size=size)
        if quantity:
            queryset = queryset.filter(quantity=quantity)
        if status:
            queryset = queryset.filter(status=status)

        return queryset