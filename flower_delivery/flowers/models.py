from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Flower(models.Model):  # товар
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='flowers/')

    def __str__(self):
        return self.name

class Order(models.Model):  # заказ
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flowers = models.ManyToManyField(Flower)
    status = models.CharField(max_length=50, default='Pending')
    date_ordered = models.DateTimeField(auto_now_add=True)

class Review(models.Model):  # отзывы
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'Review by {self.user} for {self.flower}'

class UserProfile(models.Model):  # таблица пользователей
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

class Report(models.Model):  # таблица отчетов
    date = models.DateField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sales_data = models.TextField()
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Report for {self.order} on {self.date}'

