from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    
    @property
    def sale_price(self):
        return float(self.price) - (float(self.price) * 0.05)
    
    def discount_price(self):
        return "123"