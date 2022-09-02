from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=25, null=True)
    author = models.CharField(max_length=25, null=True)
    price = models.IntegerField()
    edition = models.IntegerField()

    class Meta:
        db_table = "book"

    def __str__(self):
        return str(self.title)


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=True)
    phone = models.CharField(max_length=25, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "customer"

    def __str__(self):
        return str(self.name)


class Cart(models.Model):
    customer = models.OneToOneField(
        Customer, null=True, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)

    class Meta:
        db_table = "cart"

    def __str__(self):
        return str(self.customer)
