from django.contrib import admin
from menu.models import *
admin.site.register(Food)
@admin.register(CartItem)
class CartIteamAdmin(admin.ModelAdmin):
    list_display = ['id','cart','product','quantity','get_total_price','get_str_representation']
    def get_str_representation(self, obj):
        return str(obj)  
    get_str_representation.short_description = 'Описание'

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name_ru','name_en','name_tk']
    filter_horizontal = ('category_of_food',)


@admin.register(Category_of_food)
class Category_of_foodAdmin(admin.ModelAdmin):
    list_display = ['id','name_ru','name_en','name_tk']
    filter_horizontal = ('foods',)