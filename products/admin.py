from django.contrib import admin
from .models import Product, Category, ProductImage, StockRecord

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'parant')
    search_fields = ('name',)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class StockRecordInline(admin.StackedInline):
    model = StockRecord
    extra = 0
    max_num = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'price', 'category', 'is_active')
    search_fields = ('title', 'description')
    inlines = [ProductImageInline]
    list_filter = ('category', 'is_active')

admin.site.register(Category, CategoryAdmin)

