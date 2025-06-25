from django.db import models

class Food(models.Model):
    name_ru = models.CharField(max_length=100, blank=False, null=False)
    name_en = models.CharField(max_length=100, blank=False, null=False)
    name_tk = models.CharField(max_length=100, blank=False, null=False)
    description_ru = models.TextField(blank=False, null=False)
    description_en = models.TextField(blank=False, null=False)
    description_tk = models.TextField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)  
    image = models.ImageField(upload_to='static/image', blank=False, null=False)
    weight = models.PositiveIntegerField(null=False, blank=False)
    def get_total_price(self):
        return self.quantity * self.price

class Category(models.Model):
    name_ru = models.CharField(max_length=150, null=False, blank=False)
    name_en = models.CharField(max_length=150, null=False, blank=False)
    name_tk = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='static/image', blank=False, null=False, default='image/1.jpg')
    foods = models.ManyToManyField(Food, related_name="foods")

class Category_of_roll(models.Model):
    name_ru = models.CharField(max_length=150, null=False, blank=False)
    name_en = models.CharField(max_length=150, null=False, blank=False)
    name_tk = models.CharField(max_length=150, null=False, blank=False)
    rolls = models.ManyToManyField(Food, related_name="rolls")

class Roll(models.Model):
    name_ru = models.CharField(max_length=150, null=False, blank=False)
    name_en = models.CharField(max_length=150, null=False, blank=False)
    name_tk = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='static/image', blank=False, null=False, default='image/1.jpg')
    category_of_roll = models.ManyToManyField(Category_of_roll, related_name='category_of_roll')

class Banner(models.Model):
    image = models.ImageField(upload_to='static/image', blank=False, null=False)
    urls_of_add = models.URLField(max_length=300, blank=False, null=False)

class Imgae_of_Stories(models.Model):
    image = models.ImageField(upload_to='static/image', blank=False, null=False)

class Stories(models.Model):
    image_of_stories = models.ManyToManyField(Imgae_of_Stories, related_name='image_of_stories')

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order_CartItem(models.Model):
    order_cart = models.ForeignKey('Order_Cart', on_delete=models.CASCADE, related_name='cart_items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class TableOrderItem(models.Model):
    table_order = models.ForeignKey('Table_creat_order', on_delete=models.CASCADE, related_name='table_items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order_Cart(models.Model):
    phone_number = models.CharField(max_length=50, null=False, blank=False)
    adress = models.CharField(max_length=300, blank=False, null=False)
    list_of_foods = models.ManyToManyField(Food, through='Order_CartItem', related_name='list_of_foods')
    def get_total(self):
        return sum(item.food.price * item.quantity for item in self.cart_items.all())

class Order(models.Model):
    phone_number = models.CharField(max_length=100, null=False, blank=False)
    list_of_food = models.ManyToManyField(Food, through='OrderItem', related_name='list_of_food')
    def get_total(self):
        return sum(item.food.price * item.quantity for item in self.order_items.all())

class Table_creat_order(models.Model):
    table_number = models.PositiveBigIntegerField(null=False, blank=False)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    list_of_foods = models.ManyToManyField(Food, through='TableOrderItem', related_name='food_list')
    def get_total(self):
        return sum(item.food.price * item.quantity for item in self.table_items.all())