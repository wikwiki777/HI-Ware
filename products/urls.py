from django.urls import path
from products import views

urlpatterns = [
    path('', views.products, name='products'),
    path('motherboards/', views.products, name='motherboards'),
    path('processors/', views.products, name='processors'),
    path('graphics/', views.products, name='graphics'),
    path('<int:id>/', views.product_details, name='product_details'),
    path('search/', views.search_all, name='search'),
]