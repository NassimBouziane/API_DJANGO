from rest_framework.generics import CreateAPIView
from ..models import Product, Category
from rest_framework.response import Response
from ..serializers import ProductSerializer, CategorySerializer
from rest_framework import status


class ProductCreateView(CreateAPIView):
    http_method_names = ["post"]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        if request.auth_valid:
            return super().create(request, *args, **kwargs)
        else:
            return Response({'message': 'Authentification invalide'}, status=status.HTTP_401_UNAUTHORIZED)
        

class CategoryCreateView(CreateAPIView):
    http_method_names = ["post"]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        if request.auth_valid:
            return super().create(request, *args, **kwargs)
        else:
            return Response({'message': 'Authentification invalide'}, status=status.HTTP_401_UNAUTHORIZED)