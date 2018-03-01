from django.contrib import admin

from .models import Restaurant,Item,FavRest,FavItem

admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(FavRest)
admin.site.register(FavItem)