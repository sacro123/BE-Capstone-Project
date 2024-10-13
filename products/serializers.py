from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_date', 'user']
        read_only_fields = ['id', 'created_date', 'user']

    def validate(self, data):
        if 'price' in data and data['price'] <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        if 'stock_quantity' in data and data['stock_quantity'] < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return data
