from django.contrib import admin
from django.urls import path
from food_app import views
from django.conf.urls.static import static
from food import settings

urlpatterns = [
    
    path('home',views.home),
    path('contact',views.contact),
    path('about',views.about),

    path('login',views.user_login),
    path('logout',views.user_logout),
    path('register',views.register),
    path('menu1',views.menu12),
    path('catfiltermenu/<cv>',views.catfiltermenu),
    path('cart',views.cart),
    path('addtocart/<fid>',views.addtocart),
    path('remove/<cid>',views.remove),
    path('profile',views.user_profile),
    path('uprofile/<uid>',views.update_profile),
    path('ChangePassword/<uid>',views.change_pass),
    path('ChangePassword',views.password),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('food_details/<pid>',views.fdetails),
    path('placeorder',views.placeorder),
    path('makepayment',views.makepayment),
    path('sendmail/<uemail>/<uid>',views.sendusermail),
    path('orderHistory',views.OrderH)
    
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)