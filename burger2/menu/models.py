from django.db import models

class SVGImageField(models.FileField):
    def __init__(self, verbose_name=None, name=None, upload_to='', storage=None, **kwargs):
        super().__init__(upload_to=upload_to, storage=storage, **kwargs)
        self.verbose_name = verbose_name
        self.name = name

    def formfield(self, **kwargs):
        from .forms import SVGFormImageField
        defaults = {'form_class': SVGFormImageField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

class Food(models.Model):
    name_ru = models.CharField(
        max_length=100, 
        blank=False, 
        null=False,
        verbose_name='Название на русском',
        )
    name_en = models.CharField(
        max_length=100, 
        blank=False, 
        null=False,
        verbose_name='Название на Анлийком',
        )
    name_tk = models.CharField(
        max_length=100, 
        blank=False, 
        null=False,
        verbose_name='Название на Туркменском',
        )
    description_ru = models.TextField(
        blank=False,
        null=False,
        verbose_name='Описание на русском',
        )
    description_en = models.TextField(
        blank=False, 
        null=False,
        verbose_name='Описание на Аглийском',
        )
    description_tk = models.TextField(
        blank=False, 
        null=False,
        verbose_name='Описание на Туркменскком',
        )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name='Цена блюда',
        )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Порция или количиство',
        )  
    image = SVGImageField(
        upload_to='static/image', 
        blank=False,
        null=False,
        verbose_name='Фотография блюда',
        )
    weight = models.PositiveIntegerField(
        null=False, 
        blank=False,
        verbose_name='Его вес',
        )
    def get_total_price(self):
        return self.quantity * self.price
    def __str__(self):
        return f"{self.name_ru}"
    class Meta:
        verbose_name = "Блюда"
        verbose_name_plural = "Блюды"
class Category(models.Model):
    name_ru = models.CharField(
        max_length=150, 
        null=False, 
        blank=False,
        verbose_name='Название на русском',
        )
    name_en = models.CharField(
        max_length=150, 
        null=False, 
        blank=False,
        verbose_name='Название на Английском',
        
        )
    name_tk = models.CharField(
        max_length=150, 
        null=False, 
        blank=False,
        verbose_name='Название на Туркменском',
        )
    image = SVGImageField(
        upload_to='static/image', 
        blank=False, null=False, 
        default='image/1.jpg',
        verbose_name='Фотография',
        )
    foods = models.ManyToManyField(
        Food, 
        related_name="foods",
        verbose_name='Вьбирете блюда которые будут относитья к этому категорию',
        )
    class Meta:
        verbose_name = "Катигория Блюда"
        verbose_name_plural = "Катигория Блюд"
class Category_of_roll(models.Model):
    name_ru = models.CharField(
        max_length=150, 
        null=False, 
        blank=False,
        verbose_name='Название на русском',
        )
    name_en = models.CharField(
        max_length=150, 
        null=False, 
        blank=False,
        verbose_name='Название на Английском',
        )
    name_tk = models.CharField(
        max_length=150, 
        null=False, 
        blank=False,
        verbose_name='Название на Туркменском',
        )
    rolls = models.ManyToManyField(
        Food, 
        related_name="rolls",
        verbose_name='Вьбирете роллы которые будут относитья к этому категорию',
        )
    class Meta:
        verbose_name = "Ролл"
        verbose_name_plural = "Роллы"
class Banner(models.Model):
    image = SVGImageField(
        upload_to='static/image', 
        blank=False, 
        null=False,
        verbose_name='Фотография',
        )
    urls_of_add = models.URLField(
        max_length=300, 
        blank=False, 
        null=False,
        verbose_name='Ссылка на рекламу',
        )
    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"

class Stories(models.Model):
    name_ru = models.CharField(
        max_length=150, 
        null=False, 
        blank=False,
        verbose_name='Название на русском',
        default='ru',
        )
    name_en = models.CharField(
        max_length=150, 
        null=False, 
        blank=False,
        verbose_name='Название на Английском',
        default='ru',
        )
    name_tk = models.CharField(
        max_length=150, 
        null=False, 
        blank=False,
        verbose_name='Название на Туркменском',
        default='ru',
        )
    image = SVGImageField(
        upload_to='static/image', 
        blank=False, 
        null=False,
        verbose_name='Фотография для кружка',
        default='static/image/1.jpg',
        )
    circle = models.ImageField(
        upload_to='static/image', 
        blank=False, 
        null=False,
        verbose_name='Фотография истории',
        default='static/image/1.jpg',
        )
    class Meta:
        verbose_name = "Сторис"
        verbose_name_plural = "Сторисы"

class OrderItem(models.Model):
    order = models.ForeignKey(
        'Order', 
        on_delete=models.CASCADE,
        related_name='order_items'
        )
    food = models.ForeignKey(
        Food, 
        on_delete=models.CASCADE)
    
    quantity = models.PositiveIntegerField(
        default=1
        )

class Order_CartItem(models.Model):
    order_cart = models.ForeignKey(
        'Order_Cart', 
        on_delete=models.CASCADE, 
        related_name='cart_items'
        )
    food = models.ForeignKey(
        Food, 
        on_delete=models.CASCADE
        )
    quantity = models.PositiveIntegerField(
        default=1
        )

class TableOrderItem(models.Model):
    first_name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        default='wrvrv',
    )
    table_order = models.ForeignKey(
        'Table_creat_order', 
        on_delete=models.CASCADE, 
        related_name='table_items'
        )
    food = models.ForeignKey(
        Food, 
        on_delete=models.CASCADE
        )
    quantity = models.PositiveIntegerField(
        default=1
        )

class Order_Cart(models.Model):
    phone_number = models.CharField(
        max_length=50, 
        null=False, 
        blank=False,
        verbose_name='Телефоный номер',
        )
    adress = models.CharField(
        max_length=300, 
        blank=False, 
        null=False,
        verbose_name='Адресс',
        )
    list_of_foods = models.ManyToManyField(
        Food, 
        through='Order_CartItem', 
        related_name='list_of_foods',
        verbose_name='Список блюд заказа',
        )
    def get_total(self):
        return sum(item.food.price * item.quantity for item in self.cart_items.all())
    class Meta:
        verbose_name = "Заказ на вынос"
        verbose_name_plural = "Заказ на вынос"
class Order(models.Model):
    phone_number = models.CharField(
        max_length=100, 
        null=False, 
        blank=False,
        verbose_name='Телефоный номер',
        )
    list_of_food = models.ManyToManyField(
        Food, 
        through='OrderItem', 
        related_name='list_of_food',
        verbose_name='Список блюд заказа',
        )
    def get_total(self):
        return sum(item.food.price * item.quantity for item in self.order_items.all())
    class Meta:
        verbose_name = "Заказ на самовынос"
        verbose_name_plural = "Заказ на самовынос"
class Table_creat_order(models.Model):
    first_name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        default='wrvrv',
    )
    table_number = models.PositiveBigIntegerField(
        null=False, 
        blank=False,
        verbose_name='Намер столика',
        )
    phone_number = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        verbose_name='Телефоный номер',
        )
    list_of_foods = models.ManyToManyField(
        Food, 
        through='TableOrderItem', 
        related_name='food_list',
        verbose_name='Список блюд заказа',
        )
    def get_total(self):
        return sum(item.food.price * item.quantity for item in self.table_items.all())
    class Meta:
        verbose_name = "Заказ на столик"
        verbose_name_plural = "Заказ на столик"