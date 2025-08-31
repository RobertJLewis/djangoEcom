from django.db import models
from decimal import Decimal
from orders.models import Order


# Create your models here.
class Payment(models.Model):
    class Provider(models.TextChoices):
        STRIPE = 'stripe', 'Stripe'

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        SUCCEEDED = 'succeeded', 'Succeeded'
        FAILED = 'failed', 'Failed'
        CANCELLED = 'cancelled', 'Cancelled'

    order = models.OneToOneField('orders.Order', related_name='payments', on_delete=models.CASCADE)
    provider = models.CharField(max_length=20, choices=Provider.choices, default=Provider.STRIPE)
    provider_session_id = models.CharField(max_length=255, blank=True, db_index=True)
    status= models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    amount_cents = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=10, default='GBP')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def amount(self) -> Decimal:
        return Decimal(self.amount_cents) / 100
    
    def __str__(self):
        return f"Payment for Order #{self.order.id} - {self.status}" 
    
     