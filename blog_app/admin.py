from django.contrib import admin

# Register your models here.
from blog_app.models import*
# Register your models here.
admin.site.register([Customer,Category,Blog])