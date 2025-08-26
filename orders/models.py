from django.db import models
from django.conf import settings
from decimal import Decimal

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        PAID = 'paid', 'Paid'
        CANCELLED = 'cancelled', 'Cancelled'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=20, blank=True)

    total_cents = models.PositiveIntegerField(default=0)

    curecncy = models.CharField(max_length=3, default='GBP')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

#stripe payments
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.email} - {self.status}"
    @property
    def total(self)->Decimal:
        """
        Calculate the total amount of the order in decimal format.
        """
        return Decimal(self.total_cents) / 100
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_title = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price_cents = models.PositiveIntegerField()

    @property
    def line_cents(self):
        """
        Calculate the price of the item in decimal format.
        """
        return (self.unit_price_cents) * self.quantity

    