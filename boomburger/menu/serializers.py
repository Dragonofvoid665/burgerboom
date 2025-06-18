from rest_framework import serializers
from .models import *

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(
        queryset=Food.objects.all(), source='food', write_only=True
    )
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'food', 'food_id', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items', 'total']

    def get_total(self, obj):
        return obj.get_total()
    
# -------------------------------------------------------------------------------------------------------

class Categor_of_foodSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True,read_only=True)
    class Meta:
        model = Category_of_food
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    category_of_food = Categor_of_foodSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = '__all__'