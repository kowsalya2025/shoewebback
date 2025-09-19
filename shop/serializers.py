from rest_framework import serializers
from .models import Product  # ✅ use your actual model

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


