from django.contrib import admin
from .models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','title','event_type','target_batch','target_branch','date','time_from','time_to','remainder','remainder_date','remainder_time','description']