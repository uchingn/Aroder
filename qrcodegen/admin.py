from django.contrib import admin
from .models import *  # ✅ Import your model first

# Register your models here.
admin.site.register(Qrcode)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','content')
    