from django.contrib import admin
from . models import Branch,Sbranch,RegForm
# Register your models here.
class BranchAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Branch,BranchAdmin)

class SbranchAdmin(admin.ModelAdmin):
    list_display=['name','available']
    list_editable = ['available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page =10
admin.site.register(Sbranch,SbranchAdmin)

admin.site.register(RegForm)
