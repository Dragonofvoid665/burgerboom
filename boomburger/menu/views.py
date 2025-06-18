from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from menu.models import *
from menu.serializers import *
from users.models import User
# -----------------------------------------------------------------------------
class CartDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_object(self):
        if not isinstance(self.request.user, User):
            return Response(
                {"error": "User is not authenticated or invalid user instance"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        food_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        
        food = get_object_or_404(Food, pk=food_id)
        if food.quantity < quantity:
            return Response(
                {"error": f"Недостаточно товара '{food.name_ru}' на складе. Доступно: {food.quantity}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=food)
        
        if not item_created:
            if cart_item.quantity + quantity > food.quantity:
                return Response(
                    {"error": f"Нельзя добавить больше '{food.name_ru}'. Доступно: {food.quantity}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
        
        return Response(
            {"message": f"Товар '{food.name_ru}' добавлен в корзину"},
            status=status.HTTP_200_OK
        )

class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):
        cart_item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
        product_name = cart_item.product.name_ru
        cart_item.delete()
        return Response(
            {"message": f"Товар '{product_name}' удалён из корзины"},
            status=status.HTTP_200_OK
        )
# --------------------------------------------------------------------------------------------------------------------------------

@api_view(['GET'])
def FoodView(request,food_id):
    food = get_object_or_404(Food, id=food_id)
    serializers = FoodSerializer(food, context={'request': request})
    return Response(serializers.data)

class CategoryViews(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'options']

    def get(self, request):
        categories = self.queryset.all()
        serializer = self.serializer_class(categories, many=True, context={'request': request})
        return Response(serializer.data)