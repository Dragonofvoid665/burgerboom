from django.contrib import admin
from .models import *
from django.utils.html import format_html

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id','name_ru','name_en','name_tm','description_ru','description_en','description_tm','price','quantity','picture','weight','get_total_price']
    def picture(self, obj:Food):
        try:
            return format_html(f'<img src="{obj.image.url}" width="150px" height="150px" />')
        except:
            return None
        
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_ru', 'name_en', 'name_tm']
    filter_horizontal = ('foods', )

@admin.register(Category_of_roll)
class Category_of_rollAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_ru', 'name_en', 'name_tm']
    filter_horizontal = ('rolls', )

@admin.register(Roll)
class RollAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_ru', 'name_en', 'name_tm', ]
    filter_horizontal = ('category_of_roll', )

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'picture', 'urls_of_add']
    def picture(self, obj:Banner):
        try:
            return format_html('<img src="{obj.image.url}" width="150px" height="150px" />')
        except:
            return None
        
@admin.register(Imgae_of_Stories)
class Imgae_of_StoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'picture']
    def picture(self, obj:Imgae_of_Stories):
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
    list_display = ['id', 'phone_number', 'adress','get_total','display_food_list']
    filter_horizontal = ('list_of_foods', )
    def display_food_list(self, obj):
        food_names = [food.name_ru for food in obj.list_of_foods.all()]
        return ", ".join(food_names[:5]) + ("..." if len(food_names) > 5 else "")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','phone_number','get_total','display_food_list']
    filter_horizontal = ('list_of_food',)
    def display_food_list(self, obj):
        food_names = [food.name_ru for food in obj.list_of_food.all()]
        return ", ".join(food_names[:5]) + ("..." if len(food_names) > 5 else "")
    
@admin.register(Table_creat_order)
class Table_create_orderAdmin(admin.ModelAdmin):
    list_display = ['id','table_number','phone_number'  ,'get_total','display_food_list']
    filter_horizontal = ('list_of_foods',)
    def display_food_list(self, obj):
        food_names = [food.name_ru for food in obj.list_of_foods.all()]
        return ", ".join(food_names[:5]) + ("..." if len(food_names) > 5 else "")