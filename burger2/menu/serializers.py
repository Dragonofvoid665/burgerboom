from rest_framework import serializers
from menu.models import *

class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class CategoriesSerializars(serializers.ModelSerializer):
    foods = FoodSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class Categories_of_RollSerializers(serializers.ModelSerializer):
    rolls = FoodSerializers(many=True, read_only=True)
    class Meta:
        model = Category_of_roll
        fields = '__all__'

class RollSerializers(serializers.ModelSerializer):
    category_of_roll = Categories_of_RollSerializers(many=True, read_only=True)
    class Meta:
        model = Roll
        fields = '__all__'

class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['image', 'urls_of_add']

class StoriesImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Imgae_of_Stories
        fields = ['image']

class StoriesSerializers(serializers.ModelSerializer):
    image_of_stories = StoriesImageSerializers(many=True, read_only=True)
    class Meta:
        model = Stories
        fields = ['image_of_stories']

class OrderItemSerializer(serializers.Serializer):
    food_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

class OrderCartSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)
    list_of_foods = FoodSerializers(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order_Cart
        fields = ['phone_number', 'adress', 'items', 'list_of_foods', 'total']

    def get_total(self, obj):
        return obj.get_total()

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order_cart = Order_Cart.objects.create(**validated_data)
        for item_data in items_data:
            try:
                food = Food.objects.get(id=item_data['food_id'])
                Order_CartItem.objects.create(order_cart=order_cart, food=food, quantity=item_data['quantity'])
            except Food.DoesNotExist:
                raise serializers.ValidationError(f"Food with id {item_data['food_id']} does not exist")
        return order_cart

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)
    list_of_food = FoodSerializers(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['phone_number', 'items', 'list_of_food', 'total']

    def get_total(self, obj):
        return obj.get_total()

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            try:
                food = Food.objects.get(id=item_data['food_id'])
                OrderItem.objects.create(order=order, food=food, quantity=item_data['quantity'])
            except Food.DoesNotExist:
                raise serializers.ValidationError(f"Food with id {item_data['food_id']} does not exist")
        return order

class Tabel_create_orderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)
    list_of_foods = FoodSerializers(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Table_creat_order
        fields = ['table_number', 'phone_number', 'items', 'list_of_foods', 'total']

    def get_total(self, obj):
        return obj.get_total()

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Table_creat_order.objects.create(**validated_data)
        for item_data in items_data:
            try:
                food = Food.objects.get(id=item_data['food_id'])
                TableOrderItem.objects.create(table_order=order, food=food, quantity=item_data['quantity'])
            except Food.DoesNotExist:
                raise serializers.ValidationError(f"Food with id {item_data['food_id']} does not exist")
        return order