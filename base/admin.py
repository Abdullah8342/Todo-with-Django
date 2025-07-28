from django.contrib import admin

from .models import task
# Register your models here.


@admin.register(task)
class taskAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title','created']
    search_fields = ['title']
