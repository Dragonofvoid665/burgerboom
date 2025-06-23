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

@admin.register(Roll)
class RollAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_ru', 'name_en', 'name_tk', 'image']
    filter_horizontal = ('category_of_roll', )

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'picture', 'urls_of_add']
    def picture(self, obj: Banner):
        try:
            return format_html('<img src="{obj.image.url}" width="150px" height="150px" />')
        except:
            return None

@admin.register(Imgae_of_Stories)
class Imgae_of_StoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'picture']
    def picture(self, obj: Imgae_of_Stories):
        try:
            return format_html(f'<img src="{obj.image.url}" width="150px" height="150px" />')
        except:
            return None

@admin.register(Stories)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ['id']
    filter_horizontal = ('image_of_stories', )

@admin.register(Order_Cart)
class Order_CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'adress', 'get_total', 'display_food_list_with_quantity']
    inlines = [Order_CartItemInline]

    def display_food_list_with_quantity(self, obj):
        food_items = []
        for item in obj.cart_items.all():
            food_items.append(f"{item.food.name_ru} (Qty: {item.quantity})")
        return ", ".join(food_items[:5]) + ("..." if len(food_items) > 5 else "")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'get_total', 'display_food_list_with_quantity']
    inlines = [OrderItemInline]

    def display_food_list_with_quantity(self, obj):
        food_items = []
        for item in obj.order_items.all():
            food_items.append(f"{item.food.name_ru} (Qty: {item.quantity})")
        return ", ".join(food_items[:5]) + ("..." if len(food_items) > 5 else "")

@admin.register(Table_creat_order)
class Table_create_orderAdmin(admin.ModelAdmin):
    list_display = ['id', 'table_number', 'phone_number', 'get_total', 'display_food_list_with_quantity']
    inlines = [TableOrderItemInline]

    def display_food_list_with_quantity(self, obj):
        food_items = []
        for item in obj.table_items.all():
            food_items.append(f"{item.food.name_ru} (Qty: {item.quantity})")
        return ", ".join(food_items[:5]) + ("..." if len(food_items) > 5 else "")