from rest_framework.generics import DestroyAPIView
from ..models import Product, Category
from ..serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import status


class ProductDeleteView(DestroyAPIView):
    http_method_names = ["delete"]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        if request.auth_valid:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({'message': 'Authentification invalide'}, status=status.HTTP_401_UNAUTHORIZED)
        
class CategoryDeleteView(DestroyAPIView):
    http_method_names = ["delete"]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        if request.auth_valid:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({'message': 'Authentification invalide'}, status=status.HTTP_401_UNAUTHORIZED)