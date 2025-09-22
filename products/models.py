from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class timeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(timeStampedMixin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Category(timeStampedMixin):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    parant = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('catalog:category_detail', kwargs={'slug': self.slug})
    
class ProductImage(timeStampedMixin):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    is_primary = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_primary', 'id'] 

    def __str__(self):
        return f"Image for {self.product.name}"
    


# maybe add stock record class in future 
class StockRecord(models.Model):
    product = models.OneToOneField(Product, related_name='stock', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sku = models.CharField(max_length=30, unique=True)
    low_stock_threshold = models.PositiveIntegerField(default=5)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Stock record for {self.product.title} on {self.date}"
