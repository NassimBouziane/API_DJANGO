from rest_framework.generics import UpdateAPIView
from ..models import Product, Category
from rest_framework.response import Response
from rest_framework import status
from ..serializers import ProductSerializer, CategorySerializer

class ProductUpdateView(UpdateAPIView):
    http_method_names = ["put"]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        if request.auth_valid:
            return super().update(request, *args, **kwargs)
        else:
            return Response({'message': 'Authentification invalide'}, status=status.HTTP_401_UNAUTHORIZED)

class CategoryUpdateView(UpdateAPIView):
    http_method_names = ["put"]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        if request.auth_valid:
            return super().update(request, *args, **kwargs)
        else:
            return Response({'message': 'Authentification invalide'}, status=status.HTTP_401_UNAUTHORIZED)