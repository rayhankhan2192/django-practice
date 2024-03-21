from rest_framework import serializers
from .models import Product

class Product_Serializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'discount' #rename the field name come from model.property.method
        ]
    # def get_discount(self, obj):
    #     try:
    #         return obj.sale_discount()
    #     except:
    #         None
    def get_discount(self, obj):       
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.sale_discount()