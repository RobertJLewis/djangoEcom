from django.urls import path
from . import views 

app_name = 'catalog'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category_detail'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]