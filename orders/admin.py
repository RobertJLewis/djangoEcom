from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at', 'total_cents', 'status')
    list_filter = ('created_at', 'status')
    search_fields = ('first_name', 'last_name', 'email')
    inlines = [OrderItemInline]
    


