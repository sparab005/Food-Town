from django.contrib import admin
from .form import TopRestaurantAdminForm
from .form import FoodMenuAdminForm

from food_app.models import menus1 ,TopRestaurant,food
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display=['id','name','is_active']

# class TopRestaurantAdmin(admin.ModelAdmin):
#     list_display=['id','name','variety','is_active']

class TopRestaurantAdmin(admin.ModelAdmin):
    form = TopRestaurantAdminForm
    list_display=['id','name','variety','is_active','NickName']

class FoodMenuAdmin(admin.ModelAdmin):
    form=FoodMenuAdminForm
    list_display=['id','food','foodname','rupess','description','is_active','menuid']

# class DominoPizzaAdmin(admin.ModelAdmin):
#     form=DominoPizzaAdminForm
#     list_display=['id','food','foodname','rupess','description','is_active','resid']
#     list_filter=['food','is_active']

# class SubwayAdmin(admin.ModelAdmin):
#     form=SubwayAdminForm
#     list_display=['id','food','foodname','rupess','description','is_active','resid']

# class McDonaldsAdmin(admin.ModelAdmin):
#     form = McDonaldsAdminForm
#     list_display=['id','food','foodname','rupess','description','is_active','resid']
    

# class Belgian_WaffleAdmin(admin.ModelAdmin):
#     form=Belgian_WaffleAdminForm
#     list_display=['id','food','foodname','rupess','description','is_active','resid']

# class MenuFilterAdmin(admin.ModelAdmin):
#     form=menufilterAdminForm
#     list_display=['id','is_active','menuid','resid']
#     list_filter=['menuid','is_active']

admin.site.register(menus1,MenuAdmin)
admin.site.register(TopRestaurant,TopRestaurantAdmin)
# admin.site.register(DominoPizza,DominoPizzaAdmin)
# admin.site.register(Subway,SubwayAdmin)
# admin.site.register(menufilter,MenuFilterAdmin)
# admin.site.register(McDonalds,McDonaldsAdmin)
# admin.site.register(Belgian_Waffle,Belgian_WaffleAdmin)
admin.site.register(food,FoodMenuAdmin)






