from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class ProductReview(models.Model):
    REVIEW_TYPE_CHOICES = [
        ('positive', 'Позитивний'),
        ('negative', 'Негативний'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_email = models.EmailField()
    description = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1,6)])
    review_type = models.CharField(max_length=10, choices=REVIEW_TYPE_CHOICES)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    def __str__(self):
        return f"{self.user_email} ({self.review_type})"
