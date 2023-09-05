from django.contrib import admin
from .models import Author,Category, Blog


admin.site.register(Author)



@admin.register(Blog)
class BLogAdmin(admin.ModelAdmin):
    list_display=['title','author', 'created_at','update_at',]
    prepopulated_fields={'slug':('title',)}
    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}


