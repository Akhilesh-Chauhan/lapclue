from django.contrib import admin
from lap.models import SignUp,AcountDetails,AllProducts,Cart

# Register your models here.

admin.site.register(SignUp)
class PostAdmin(admin.ModelAdmin):
    list_display=('name','email','phoneno')
    list_filter=('email',)
    search_fields=['name','email']
admin.site.register(AcountDetails,PostAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','cname','modelno','category','price','screen','processor','graphics','memory')
    list_filter=('category',)
    search_fields=['cname','modelno','category']
admin.site.register(AllProducts,PostAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','cname','modelno','category')
    list_filter=('category',)
    search_fields=['cname','modelno','category']
admin.site.register(Cart,PostAdmin)