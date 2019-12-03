from django.contrib import admin
from .models import Course,Batch,Role,ClassRoom,Hr,Trainer,TimeTable,User,Placement,Feedback

# Register your models here.
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Role)
admin.site.register(ClassRoom)
admin.site.register(Hr)
admin.site.register(Trainer)
admin.site.register(TimeTable)
admin.site.register(User)
admin.site.register(Placement)
admin.site.register(Feedback)

