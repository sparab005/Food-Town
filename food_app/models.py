from django.db import models
from django.contrib.auth.models import User

class menus1(models.Model):

    name=models.CharField(max_length=50, verbose_name ="menu ")
    is_active=models.BooleanField(default=True, verbose_name ="Active")
    pimage=models.ImageField(upload_to='image')
    

 
    
class TopRestaurant(models.Model):
    name = models.CharField(max_length=50, verbose_name="Restaurant")
    variety = models.CharField(max_length=32, verbose_name="variety")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    pimage = models.ImageField(upload_to='image')
    NickName = models.CharField(max_length=50)

class food(models.Model):
    CAT=((1,'Veg'),(2,'Non Veg'))
    
   
    menuid=models.ForeignKey(menus1,on_delete=models.CASCADE,db_column="menuid" )
    food=models.IntegerField( verbose_name ="Food ",choices=CAT)
    foodname=models.CharField(max_length=150, verbose_name ="FoodName ")
    rupess=models.BigIntegerField(verbose_name="Cost")
    description=models.CharField(max_length=500, verbose_name ="Description ")
    is_active=models.BooleanField(default=True, verbose_name ="Active")
    pimage=models.ImageField(upload_to='image')



# class McDonalds(models.Model):
    
#     CAT=((1,'Veg'),(2,'Non Veg'))
    
   
#     resid=models.ForeignKey(TopRestaurant,on_delete=models.CASCADE,db_column="resid" )
#     food=models.IntegerField( verbose_name ="Food ",choices=CAT)
#     foodname=models.CharField(max_length=50, verbose_name ="FoodName ")
#     rupess=models.BigIntegerField(verbose_name="Cost")
#     description=models.CharField(max_length=500, verbose_name ="Description ")
#     is_active=models.BooleanField(default=True, verbose_name ="Active")
#     pimage=models.ImageField(upload_to='image')

   
   

# class DominoPizza(models.Model):
#     CAT=((1,'Veg'),(2,'Non Veg'))
#     resid=models.ForeignKey(TopRestaurant,on_delete=models.CASCADE,db_column="resid" ,default=1)
#     food=models.IntegerField( verbose_name ="Food ",choices=CAT)
#     foodname=models.CharField(max_length=50, verbose_name ="FoodName ")
#     rupess=models.BigIntegerField(verbose_name="Cost")
#     description=models.CharField(max_length=150, verbose_name ="Description ")
#     is_active=models.BooleanField(default=True, verbose_name ="Active")
#     pimage=models.ImageField(upload_to='image')
    
    
                                 
# class Subway(models.Model):
    
#     CAT=((1,'Veg'),(2,'Non Veg'))

#     resid=models.ForeignKey(TopRestaurant,on_delete=models.CASCADE,db_column="resid" ,default=2)
#     food=models.IntegerField( verbose_name ="Food ",choices=CAT)
#     foodname=models.CharField(max_length=150, verbose_name ="FoodName ")
#     rupess=models.BigIntegerField(verbose_name="Cost")
#     description=models.CharField(max_length=500, verbose_name ="Description ")
#     is_active=models.BooleanField(default=True, verbose_name ="Active")
#     pimage=models.ImageField(upload_to='image')
    
    
    






 # res_name=((1,'Dominos Pizza'),(2,'subway'),(3,'McDonalds'),(4,'The Belgian Waffle'),(5,'KFC'),
    #           (6,'Gopalas Veg Kitchen'),(7,'Munchies N More'),(8,'Fatboy China'),(9,'Veg24'),(10,'Baskin Robbins'),
    #           (11,'Food O Clock'),(12,'Biryani By Kilo'),(13,'Pizza Point'),(14,'The south spice'),(15,'Deliure & The Eatrium'),
    #           (16,'Burger King'),(17,'Bake Ur Day - Cakes'),(18,'Wendys Burgers'),(19,'Pizza Hut'),(20,'Grandmamas Cafe'),
    #           (21,'Jumboking Indian Burger'),(22,'La Pinoz Pizza'),(23,'Pizza Corner'),(24,'Cantonese'),(25,'Casa Blanca'	),)

# class Belgian_Waffle(models.Model):
    
#     CAT=((1,'Veg'),(2,'Non Veg'))

#     resid=models.ForeignKey(TopRestaurant,on_delete=models.CASCADE,db_column="resid" ,default=4)
#     food=models.IntegerField( verbose_name ="Food ",choices=CAT)
#     foodname=models.CharField(max_length=50, verbose_name ="FoodName ")
#     rupess=models.BigIntegerField(verbose_name="Cost")
#     description=models.CharField(max_length=500, verbose_name ="Description ")
#     is_active=models.BooleanField(default=True, verbose_name ="Active")
#     pimage=models.ImageField(upload_to='image')


# class menufilter(models.Model):
#     resid = models.ForeignKey(TopRestaurant, on_delete=models.CASCADE, db_column="resid")
#     menuid=models.ForeignKey(menus1,on_delete=models.CASCADE,db_column="menuid")
#     is_active = models.BooleanField(default=True, verbose_name="Active")




class customer_details(models.Model):
    
    uname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    firstname=models.CharField(max_length=50,null=True)
    lastname=models.CharField(max_length=50,null=True)
    mobile=models.BigIntegerField(null=True)
    address=models.CharField(max_length=350,null=True)
    is_active=models.BooleanField(default=True, verbose_name ="Active")

class cart_page(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    fid=models.ForeignKey(food,on_delete=models.CASCADE,db_column="fid" )
    qty=models.IntegerField(default=1)
    is_active = models.BooleanField(default=True, verbose_name="Active")


class orderP (models.Model):
   
   
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    
    pid=models.ForeignKey(food,on_delete=models.CASCADE,db_column="pid")
    cid=models.ForeignKey(cart_page,on_delete=models.CASCADE,db_column="cid")
    rupess=models.FloatField()
    qty=models.IntegerField(default=1)

class OrderConfirmed (models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(food,on_delete=models.CASCADE,db_column="pid")
    rupess=models.FloatField()
    qty=models.IntegerField(default=1)