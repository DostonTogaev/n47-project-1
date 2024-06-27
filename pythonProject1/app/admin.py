from django.contrib import admin
from django.contrib.auth.models import User, Group

from app.models import Product, Images, Attributes, AttributeKey, AttributeValue, AttributeProduct

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'price', 'discount', 'quantity', 'is_amount')

    def is_amount(self, obj):
        return obj.quantity > 4

    is_amount.boolean = True
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('image', 'product')

admin.site.register(Attributes)
admin.site.register(AttributeKey)
admin.site.register(AttributeValue)
admin.site.register(AttributeProduct)





#admin.site.unregister(User)
#admin.site.unregister(Group)


