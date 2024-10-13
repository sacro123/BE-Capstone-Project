from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from .permissions import IsAuthenticatedOrReadOnly
from .pagination import CustomPagination

import logging

logger = logging.getLogger(__name__)

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'category', 'description']
    ordering_fields = ['name', 'price', 'created_date', 'stock_quantity']
    pagination_class = CustomPagination


    def perform_create(self, serializer):
        logger.info(f"Attempting to create product for user: {self.request.user}")
        try:
            if self.request.user.is_authenticated:
                serializer.save(user=self.request.user)
            else:
                serializer.save()
            logger.info("Product created successfully")
        except Exception as e:
            logger.error(f"Error creating product: {str(e)}")
            raise
    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
