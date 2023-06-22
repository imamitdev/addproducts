from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['productname','description','price','created']
    list_filter=['productname','price']
    order_by=['-created']
    search_fields=["productname"]
    
admin.site.register(Product,ProductAdmin)