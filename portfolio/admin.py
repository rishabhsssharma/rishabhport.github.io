from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(contact)




class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','description','authname','img','timeStamp' )
    search_fields =('title','description','authname')
admin.site.register(Blog,BlogAdmin)