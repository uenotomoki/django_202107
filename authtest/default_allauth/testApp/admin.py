from django.contrib import admin
from .models import SnsMessageModel,Image

# Register your models here.

admin.site.register(SnsMessageModel)

admin.site.register(Image)