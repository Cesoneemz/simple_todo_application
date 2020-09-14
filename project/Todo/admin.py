from django.contrib import admin

# Register your models here.
from Todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'done')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description', 'date', 'done')
    list_editable = ('done', )
    list_filter = ('done', )


admin.site.register(Todo, TodoAdmin)