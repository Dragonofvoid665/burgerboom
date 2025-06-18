from django.db import models
from users.models import User

class Food(models.Model):
    name_ru = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        )
    name_en = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        )
    name_tk = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        )
    description_ru = models.TextField(
        blank=False,
        null=False
        )
    description_en = models.TextField(
        blank=False,
        null=False
        )
    description_tk = models.TextField(
        blank=False,
        null=False
        )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to='static/images',
        blank=False,
        null=False,
    )
    weight = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_ru
class Category_of_food(models.Model):
    name_ru = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )
    name_en = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )
    name_tk = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )
    foods = models.ManyToManyField(Food,related_name="foods")
    def __str__(self):
        return self.name_ru

class Category(models.Model):
    name_ru =models.CharField(
        max_length=150,
        blank=False,
        null=False,
    )
    name_en = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )
    name_tk = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )
    category_of_food = models.ManyToManyField(Category_of_food,related_name='category_of_food')
    def __str__(self):
        return self.name_ru

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user}"

    def get_total(self):
        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name_ru} in {self.cart}"

    def get_total_price(self):
        return self.quantity * self.product.price   