from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.

class Logo(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, help_text="Product name")
    slug = models.SlugField(max_length=200, unique=True, blank=True, help_text="URL-friendly version of name")
    description = models.TextField(blank=True, null=True, help_text="Product description (optional)")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Product price in USD")
    image = CloudinaryField('image', help_text="Product image")
    is_active = models.BooleanField(default=True, help_text="Is this product available for sale?")
    is_recommended = models.BooleanField(default=False, help_text="Show in 'We Recommend' section?")
    stock_quantity = models.IntegerField(default=0, help_text="Available stock (0 = unlimited)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_recommended', '-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Auto-generate slug from name if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def in_stock(self):
        """Check if product is in stock (0 = unlimited stock)"""
        return self.stock_quantity == 0 or self.stock_quantity > 0

    @property
    def formatted_price(self):
        """Return formatted price string"""
        return f"${self.price:.2f}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    order_number = models.CharField(max_length=50, unique=True, editable=False)
    email = models.EmailField()
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    
    # Shipping Address
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    
    # Order Info
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    
    # Paystack Payment Fields (NEW)
    paystack_reference = models.CharField(max_length=100, blank=True, null=True, help_text="Paystack transaction reference")
    payment_status = models.CharField(max_length=20, default='pending', help_text="Payment status: pending, paid, failed")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order {self.order_number} - {self.full_name}"

    def save(self, *args, **kwargs):
        if not self.order_number:
            # Generate unique order number
            import uuid
            self.order_number = f"SN-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price at time of purchase")

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f"{self.quantity}x {self.product.name} in {self.order.order_number}"

    @property
    def subtotal(self):
        if self.quantity is None or self.price is None:
            return 0
        return self.quantity * self.price
