from django.urls import path
from django.views.generic import TemplateView
from menu import views
urlpatterns = [
    path('',TemplateView.as_view(template_name='main.html'), name='menu'),
    path('cart/', views.CartDetailView.as_view(), name='cart_detail'),
    path('cart/add/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
]