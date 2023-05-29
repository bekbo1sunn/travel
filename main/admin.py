from django.contrib import admin
from .models import Country, Category, Tiket, CategoryTikets

admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Tiket)
admin.site.register(CategoryTikets)

