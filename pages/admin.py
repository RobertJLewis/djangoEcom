from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'user', 'ip_address')
    search_fields = ('name', 'email', 'enquiry', 'user__username')
    readonly_fields = ('name', 'email', 'enquiry', 'user', 'ip_address', 'created_at')