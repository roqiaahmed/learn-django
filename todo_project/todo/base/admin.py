from django.contrib import admin
from .models import Task

# Register your models here.
# admin.site.register(Task)


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "compiled")


admin.site.register(Task, TaskAdmin)
