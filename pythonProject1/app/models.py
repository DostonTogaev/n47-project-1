from django.db import models

# Create your models here.
class Product(models.Model):
    class RatingChoice(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    discount = models.IntegerField()
    quantity = models.IntegerField(default=1)
    rating = models.IntegerField(choices=RatingChoice, default=RatingChoice.zero.value)
    attributes = models.ManyToManyField('Attributes', blank=True, related_name='attributes')

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def discount_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name

class Images(models.Model):
    image = models.ImageField(upload_to="products")
    product =models.ForeignKey('app.Product', on_delete=models.CASCADE, related_name='images')

class Attributes(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name