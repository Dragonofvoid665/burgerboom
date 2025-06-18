from django.urls import path, include
from django.contrib import admin
from menu import views
urlpatterns = [
    path('admin/',admin.site.urls),
    path('users/', include('users.urls')),
    path('api/',include('menu.urls')),
    path('food/<int:food_id>/',views.FoodView),
    path('categories/',views.CategoryViews.as_view())
]