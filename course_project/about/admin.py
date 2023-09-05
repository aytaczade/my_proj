from django.contrib import admin
from .models import About, AboutPoint, Store, SocialMedia




class InlinePointAdmin(admin.TabularInline):
    model=AboutPoint
    extra=1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines=(InlinePointAdmin,)
    
    
admin.site.register(Store)
admin.site.register(SocialMedia)