from django.shortcuts import render 
from django.views.generic import ListView, DetailView
from .models import Product, Category

# Create your views here.
class ProductListView(ListView):
    queryset = Products.objects.filter(is_active=True).select_related('category')
    template_name = 'cataloge/index.html'
    paginate_by = 12

class CategoryView(ListView):
    template_name= 'cataloge/category.html'
    paginate_by = 12
    def get_queryset(self):
        self.catagory= Category.objects.get(slug=self.kwargs['slug'])
        return(
            self.catagory.products.filter(is_active=True)
            .select_related('category')
            .prefetch_related('images')
        )
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category'] = self.catagory
        return ctx
    
class ProductDetailView(DetailView):
    queryset = Product.objects.filter(is_active=True).prefetch_related('images', 'stock')
    template_name = 'cataloge/product_detail.html'
