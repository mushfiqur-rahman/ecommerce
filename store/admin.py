from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status']
    list_editable = ['unit_price']
    list_per_page = 10

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'


admin.site.register(models.Collection)

"""  
if you use decorate like @admin.register(models.Product) 
then no need to use this line
"""


# admin.site.register(models.Product, ProductAdmin)

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
