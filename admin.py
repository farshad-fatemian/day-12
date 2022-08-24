from django.contrib import admin

from .models import Product , Comments , Picture , Category , Tag , Toptrend ,Productget , Newarrival , DiscountedProducts

# Register your models here.

class commentinline(admin.StackedInline):
    model = Comments
    
class productinline(admin.StackedInline):
    model = Productget
    
class PictureInline(admin.StackedInline):
    model = Picture
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price",'id']
    list_filter = ['price']
    search_fields= ["name"]
    inlines = [PictureInline,commentinline]
    
    
class NewarrivalAdmin(admin.ModelAdmin):
    inlines = [productinline]
    
    

    


admin.site.register(Product,ProductAdmin)
admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Toptrend)
admin.site.register(Newarrival,NewarrivalAdmin)
admin.site.register(DiscountedProducts)