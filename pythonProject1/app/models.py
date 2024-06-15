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

    def get_attributes(self) -> list[dict]:
        product_attributes = AttributeProduct.objects.filter(product=self)
        attributes = []
        for pa in product_attributes:
            attributes.append({
                'attribute_key': pa.attribute.key_name,
                'attribute_value': pa.attribute_value.value_name
            })  # [ {},{},{}]
        return attributes

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

class AttributeKey(models.Model):
    key_name = models.CharField(max_length=125, unique=True)

    def __str__(self):
        return self.key_name


class AttributeValue(models.Model):
    value_name = models.CharField(max_length=125, unique=True)

    def __str__(self):
        return self.value_name


class AttributeProduct(models.Model):
    product = models.ForeignKey('app.Product', on_delete=models.CASCADE)
    attribute = models.ForeignKey('app.AttributeKey', on_delete=models.CASCADE)
    attribute_value = models.ForeignKey('app.AttributeValue', on_delete=models.CASCADE)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    Billing_address = models.CharField(max_length=100)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

