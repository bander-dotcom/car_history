from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Users, Cars, Accidents, ImageAccident, ImageCar, Reports, Evaluation, WorkshopsData

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    llist_display = ('user_id', 'username', 'email') # بعد (صحيح)
    search_fields = ('username', 'email')

@admin.register(Cars)
class CarAdmin(admin.ModelAdmin):
    list_display = ('vin', 'report', 'model', 'make', 'year')
    search_fields = ('vin', 'report__report_id')

@admin.register(Accidents)
class AccidentAdmin(admin.ModelAdmin):
    list_display = ('accident_id','accident_date', 'damaged_parts','created_at')
    search_fields = ('car__vin', 'type_accident')

admin.site.register(ImageAccident)
admin.site.register(ImageCar)
admin.site.register(Reports)
admin.site.register(Evaluation)
admin.site.register(WorkshopsData)
