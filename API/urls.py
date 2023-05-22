from django.urls import path
from rest_framework import routers
from .api import ProductViewSet, CategoryViewSet, ProductCreateView, CategoryCreateView,ProductUpdateView,CategoryUpdateView,ProductDeleteView,CategoryDeleteView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),


]

urlpatterns += router.urls
