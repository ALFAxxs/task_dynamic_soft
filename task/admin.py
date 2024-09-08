from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'