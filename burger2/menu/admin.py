from django.contrib.admin import AdminSite
from django.contrib import admin
from menu.models import *
from django.utils.html import format_html
class Order_CartItemInline(admin.TabularInline):
    model = Order_CartItem
    extra = 1  
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
class TableOrderItemInline(admin.TabularInline):
    model = TableOrderItem
    extra = 1

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_ru', 'name_en', 'name_tk', 'description_ru', 'description_en', 'description_tk', 'price', 'quantity', 'picture', 'weight', 'get_total_price']
    def picture(self, obj: Food):
        try:
            return format_html(f'<img src="{obj.image.url}" width="150px" height="150px" />')
        except:
            return None

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_ru', 'name_en', 'name_tk', 'image']
    filter_horizontal = ('foods', )

@admin.register(Category_of_roll)
class Category_of_rollAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_ru', 'name_en', 'name_tk']
    filter_horizontal = ('rolls', )

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'picture', 'urls_of_add']
    def picture(self, obj: Banner):
        try:
            return format_html(f'<img src="{obj.image.url}" width="150px" height="150px" />')
        except:
            return None

@admin.register(Stories)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ['id','name_ru','name_en','name_tk','picture','picture2']
    def picture(self, obj: Stories):
        try:
            return format_html(f'<img src="{obj.image.url}" width="150px" height="150px" />')
        except:
            return None
    def picture2(self, obj: Stories):
        try:
            return format_html(f'<img src="{obj.circle.url}" width="150px" height="150px" />')
        except:
            return None

class OrdersAdminSite(AdminSite):
    site_header = "Админ-панель заказов"
    site_title = "Портал администрирования заказов"
    index_title = "Добро пожаловать в админ-панель заказов"

orders_admin_site = OrdersAdminSite(name='orders_admin')
class Order_CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'adress', 'get_total', 'Список_заказов_Блюда_и_его_количество']
    inlines = [Order_CartItemInline]

    def Список_заказов_Блюда_и_его_количество(self, obj):
        food_items = []
        for item in obj.cart_items.all():
            food_items.append(f"{item.food.name_ru} (количество: {item.quantity})")
        return ", ".join(food_items[:5]) + ("..." if len(food_items) > 5 else "")
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'get_total', 'Список_заказов_Блюда_и_его_количество']
    inlines = [OrderItemInline]

    def Список_заказов_Блюда_и_его_количество(self, obj):
        food_items = []
        for item in obj.order_items.all():
            food_items.append(f"{item.food.name_ru} (количество: {item.quantity})")
        return ", ".join(food_items[:5]) + ("..." if len(food_items) > 5 else "")

class Table_create_orderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'table_number', 'phone_number', 'get_total', 'Список_заказов_Блюда_и_его_количество']
    inlines = [TableOrderItemInline]

    def Список_заказов_Блюда_и_его_количество(self, obj):
        food_items = []
        for item in obj.table_items.all():
            food_items.append(f"{item.food.name_ru} (количество: {item.quantity})")
        return ", ".join(food_items[:5]) + ("..." if len(food_items) > 5 else "")
    

orders_admin_site.register(Order, OrderAdmin)
orders_admin_site.register(Order_Cart, Order_CartAdmin)
orders_admin_site.register(Table_creat_order, Table_create_orderAdmin)