from django.contrib import admin
from .models import Helpline

# Register your models here.


@admin.register(Helpline)
class HelplineAdmin(admin.ModelAdmin):
    list_display = ('name' , 'number' , 'category')
    search_fields = ('name' , 'number' , 'category')
    list_filter = ('category' ,)