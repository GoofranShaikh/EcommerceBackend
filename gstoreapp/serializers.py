from rest_framework import serializers
from .models import category,products

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields=(
            "id",
            "name",
            "slug"
        )

class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields=(
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"

            
        


        )
