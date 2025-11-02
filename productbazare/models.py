from django.db import models
from django.core.validators import MinLengthValidator

class Registeracount(models.Model):
    USER_TYPES = [
        ("customer", "ক্রেতা"),
        ("seller", "বিক্রেতা"),
        ("delivery_person", "ডেলিভারি পার্সন"),
    ]
     
    name = models.CharField(max_length=150, verbose_name="সম্পূর্ণ নাম")
    contact = models.CharField(max_length=15, verbose_name="মোবাইল নম্বর")
    address = models.TextField(verbose_name="সম্পূর্ণ ঠিকানা")
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name="প্রোফাইল ছবি")
    password = models.CharField(
        max_length=128,
        verbose_name="পাসওয়ার্ড",
        validators=[MinLengthValidator(8)]
    )
    user_type = models.CharField(max_length=20,choices=USER_TYPES, verbose_name="ব্যবহারকারীর ধরন",default="customer",blank=True,null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.contact}"
# Product model for items to buy/sell

# models.py
# models.py
 

class Product(models.Model):
    UNIT_CHOICES = [
        ('bag', 'Bag'),
        ('liter', 'Liter'),
        ('piece', 'Piece'),
        ('kg', 'Kilogram'),
        ('meter', 'Meter'),
    ]

    catagoris = models.CharField(max_length=100, default='general')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='piece')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # ✅
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.stock} {self.unit})"




# Order model for tracking purchases
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    buyer_name = models.CharField(max_length=150)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} x {self.product.name} by {self.buyer_name}"
    
    

class AddImageSlide(models.Model):
    image = models.ImageField(upload_to='slide_images/', blank=True, null=True)
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name