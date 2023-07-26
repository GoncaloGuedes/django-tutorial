from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    get_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
            model = Product
            fields = ['id', 
                      'title',  
                      'price', 
                      'sale_price',
                      'get_discount',
                      ]
    