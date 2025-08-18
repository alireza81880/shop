

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Product(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=10)
    image=models.ImageField()
    quantity=models.PositiveBigIntegerField()
    status=models.BooleanField(default=True)
    create_at=models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.title



class Cart(models.Model):
    quantity=models.PositiveBigIntegerField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Order(models.Model):
    total_price=models.DecimalField(decimal_places=2,max_digits=10) 
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.BooleanField(null=True)
    create_at=models.DateField(auto_now_add=True)

class OrderProduct(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.DecimalField(decimal_places=2,max_digits=10)

class PaymentLog(models.Model):
    amount=models.DecimalField(decimal_places=2,max_digits=10)
    create_at=models.DateField(auto_now_add=True)
    user_id=models.PositiveBigIntegerField()
    order_id=models.PositiveBigIntegerField()
    status=models.CharField(max_length=100)
    error_code=models.CharField(max_length=200)
