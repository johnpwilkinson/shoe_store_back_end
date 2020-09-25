from rest_framework import serializers

from Shoes.models import Shoe, ShoeColor, ShoeType, Manufacturer

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Manufacturer
        fields = [
            'id',
            'name',
            'website'
        ]

class ShoeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= ShoeType
        fields = [
            'id',
            'style'
        ]

class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model= ShoeColor
        fields = [
            'id',
            'color_name'
        ]

class ShoeSerializer(serializers.ModelSerializer):
    manufacturer = serializers.StringRelatedField()
    color = serializers.StringRelatedField()
    shoe_type = serializers.StringRelatedField()

    class Meta:
        model= Shoe
        fields = [
            'id',
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
        ]