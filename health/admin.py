from django.contrib import admin
from .models import Todo

admin.site.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'created_at')
    list_filter = ('completed',)
    search_fields = ('title',)

# Register your models here.
