from django.contrib import admin
from django.urls import path,include
from menu import views

urlpatterns = [
    path('food_detail/<int:food_id>/',views.Fooddetail),
    path('categories/',views.CategoryViews.as_view()),
    path('roll_list/',views.Roll_listView.as_view()),
    path('roll_detail/<int:roll_id>/',views.Roll_detail),
    path('banner/',views.BannerView.as_view()),
    path('stories/',views.StoriesView.as_view()),
    path('order/', views.CreateOrder),
    path('selforder/',views.OrderView),
    path('table_order/',views.Table_create_orderView)
]
