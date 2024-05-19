from django.contrib import admin

from .models import Video, WebPage

# Register your models here.
@admin.register(WebPage)
class WebPageAdmin(admin.ModelAdmin):
    list_display = ('title',) 

admin.site.register(Video)