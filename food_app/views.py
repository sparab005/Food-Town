from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from food_app.models import menus1 ,TopRestaurant,cart_page,customer_details,food,orderP,OrderConfirmed
from django.db.models import Q 
import random
import razorpay
from django.core.mail import send_mail


# from django.core.mail import send_mail

# Create your views here.
def home(request):
     return render(request,'index.html')

def contact(request):
     return render(request,'contact.html')

def about(request):
     return render(request,'about.html')

def user_login(request):
    if request.method =='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        context={}
        if uname=="" or upass=="":
            context['errmsg']="Fields can not be empty"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname ,password=upass)
            if u is not None:
                login(request,u)
                return redirect('/home')
            else:
                context['errmsg']="Username and password is  incorrect"
                return render(request,'login.html',context)
           
    else:
        return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect("/home")

def register(request):
        if request.method =='POST':
            uname=request.POST['uname']
            email=request.POST['email']
            
            upass=request.POST['upass']
            ucpass=(request.POST['ucpass'])
            
            upass1=make_password(upass)
            context={}
            if uname=="" or upass=="" or ucpass=="" or email=="" :
                context['errmsg']="Fields can not be empty"
                return render(request ,'register.html',context)
            elif upass!=ucpass:
                context['errmsg']="Password is not matching "
                return render(request ,'register.html',context)

            else:
                if User.objects.filter(username=uname).exists():
                    context['errmsg']="Username already exist"
                    return render(request ,'register.html',context)
                elif User.objects.filter(email=email).exists():
                    context['errmsg']="Email already exist"
                    return render(request ,'register.html',context)
                
                else:
                    
                        u=User.objects.create(password=upass1,username=uname,email=email)
                        u.save()
                        u=customer_details.objects.create(uname=uname,email=email)
                        u.save()
                        context['success']='User created successfully, Please try to '
                        return render(request,'register.html',context)
        else:
            return render(request,'register.html')




# def menu1(request):
    
#     context={}
#     p=menus1.objects.filter(is_active=True)
#     context['menu']=p
#     return render (request,'menu.html',context)

def menu12(request):
   
    context={}
    
    p=food.objects.filter(is_active=True)
    context['foodmenu']=p

    q=menus1.objects.filter(is_active=True)
    context['menu']=q
   
    return render (request,'menu1.html',context)

def fdetails(request,pid):
    p=food.objects.filter(id=pid)
    context={}
    context['food']=p
    return render(request,'food_details.html',context)



def Restaurant(request):
    context={}
    p=TopRestaurant.objects.filter(is_active=True)
    context['Restaurant']=p
    return render (request,'Restaurant.html',context)

# def Domino(request):
#     context={}
#     p=DominoPizza.objects.filter(is_active=True)
#     context['food']=p
#     return render (request,'Domino Pizza.html',context)
   
# def subway(request):
#     context={}
#     p=Subway.objects.filter(is_active=True)
#     context['food']=p
#     return render(request,'Subway.html',context)

# def McDonald(request):
#     context={}
#     p=McDonalds.objects.filter(is_active=True)
#     context['food']=p
#     return render (request,'McDonalds.html',context)

# def catfilter(request,rid,cv):
#     q1=Q(is_active=True)
#     q2=Q(food=cv)
#     if rid =='Domino Pizza':
#         p=DominoPizza.objects.filter(q1 & q2)
#         context={}
#         context['food']=p
#         return render (request,'Domino Pizza.html',context)
#     elif rid == 'subway':
#         p=Subway.objects.filter(q1 & q2)
#         context={}
#         context['food']=p
#         return render (request,'Subway.html',context)
#     elif rid =='McDonalds':
#         p=McDonalds.objects.filter(q1 & q2)
#         context={}
#         context['food']=p
#         return render (request,'McDonalds.html',context)
    

def catfiltermenu(request,cv):
    
    q1=Q(is_active=True)
    q2=Q(menuid=cv)
    p=food.objects.filter(q1 & q2)
    q=menus1.objects.filter(id=cv)
    
    

    context={}
    context['menuRestaurant']=p
    context['menu']=q
    
    # context['Restaurant']=r
    return render (request,'menu1.html',context)


def cart(request):
    context={}
    d=User.objects.filter(username=request.user.username)
    c=cart_page.objects.filter(uid=request.user.id)
    p=customer_details.objects.filter(uname=request.user.username)
    # print(c) 
    # print(c)
    np=len(c)
    s=0
    for x in c:
        # print(x)
        s=s+x.fid.rupess * x.qty
        
        
   
    if not cart_page.objects.filter(uid=request.user.id).exists():
        context['errmsg']="Cart is Empty"
        context['data']=d
        context['data1']=p
        return render(request,'cart.html',context)

    
    context['n']=np
    context['total']=s
    context['data']=d
    context['data1']=p
    context['cart']=c
    return render(request,'cart.html',context)



def addtocart(request, fid):
    
    if request.user.is_authenticated:
        userid=request.user.id
        u=User.objects.filter(id=userid)
        # print(u[0])
        p=food.objects.filter(id=fid)
        # print(p[0])

        q1=Q(uid=u[0])
        q2=Q(fid=p[0])
        c=cart_page.objects.filter(q1 & q2)
        n=len(c)
        context={}
        context['food']=p
        if n == 1:
            context['msg']="Food already exists in cart !!"
            return render(request,'food_details.html',context)
        else :
            c=cart_page.objects.create(uid=u[0],fid=p[0])
            c.save()
            # return HttpResponse("data is fetched")
            context['success']="Food Added Successfully in Cart !!"
            return render(request,'food_details.html',context)
    else:
        return redirect('/login')
    
    
def remove(request,cid):
    m=cart_page.objects.filter(id=cid)
    m.delete()
    k=orderP.objects.filter(id=cid)
    k.delete()
    return redirect('/cart')
    
def user_profile(request):
    c=User.objects.filter(username=request.user.username)
    context={}
    context['data']=c
    p=customer_details.objects.filter(uname=request.user.username)
    context['data1']=p
    return render(request,'profile.html',context)

def update_profile(request,uid):
    if request.method == 'POST':
        
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        mobile=request.POST['mobile']
        address=request.POST['address']
        context={}
        c=User.objects.filter(username=request.user.username)
        context['data']=c
        p=customer_details.objects.filter(uname=request.user.username)
        context['data1']=p
        m=User.objects.filter(id=uid)
        m.update(first_name=firstname,last_name=lastname)   
        m=customer_details.objects.filter(uname=request.user.username)
        m.update(firstname=firstname,lastname=lastname,mobile=mobile,address=address) 
        context['success']='Profile updated successfully,'
        return render(request,'profile.html',context)  
    else:
        return redirect('/profile')
    

def password(request):
    context={}
    c=User.objects.filter(username=request.user.username)
    # t=User.objects.get(id=request.user.id)
    # o=t.password
    
    context['data']=c
    return render(request,'change_password.html',context) 

def change_pass(request,uid ):
    
    if request.method == 'POST':
        uname=request.POST['uname']
        passw=request.POST['passw']
        newpass=request.POST['newpass']
        confirmpass=request.POST['confrimpass']
        upass1=make_password(confirmpass)
        context={}
        c=User.objects.filter(username=request.user.username)
        u=authenticate(username=uname,password=passw)
       
        
        if passw=="" or newpass=="" or confirmpass=="" :
                context['data']=c
                context['errmsg']="Fields can not be empty"
                return render(request ,'change_password.html',context)
        elif newpass!=confirmpass:
            context['data']=c
            context['errmsg']="Password is not matching "
            return render(request ,'change_password.html',context)
        else:
            u=authenticate(username=uname,password=passw)
            if u is not None:
                m=User.objects.filter(id=uid)
                m.update(password=upass1)
                context['data']=c
                context['success']='Password updated successfully,'
                return render(request ,'change_password.html',context)   
    else:

        return redirect('/ChangePassword') 
    

def updateqty(request,qv,cid):
    c=cart_page.objects.filter(id=cid)
    print(c[0])
    if qv == '1':
        t=c[0].qty + 1
        c.update(qty=t)
    else:
        if c[0].qty > 1 :
            t=c[0].qty - 1
            c.update(qty=t)
    return redirect('/cart')

def placeorder(request):
    d=User.objects.filter(username=request.user.username)
    p=customer_details.objects.filter(uname=request.user.username)
    context={}
    context['data']=d
    context['data1']=p


    userid=request.user.id
    carts = cart_page.objects.filter(uid=userid)
    info =""
    

    for cart in carts:
        foodname=cart.fid.foodname
        rupess=cart.fid.rupess  * cart.qty
        info+= f"Food name: {foodname}\nRupess: {rupess}"
        np=len(carts)
        s=0 
        for x in carts:
            

            s=s+x.fid.rupess * x.qty

            context['total']=s
            context['n']=np
        
    
        orders_for_cart = orderP.objects.filter(cid=cart)
        
        if orders_for_cart.exists():
            for order in orders_for_cart:
                order.delete()
        
        
        o = orderP.objects.create(cid=cart,pid=cart.fid,uid=cart.uid,qty=cart.qty,rupess=rupess)
        o.save()
        Orders=orderP.objects.filter(uid=request.user.id)
        
        context['item']=Orders
    print("price =" ,info)
        
    if not orderP.objects.filter(uid=request.user.id).exists():
        context['errmsg']="Order page is Empty ,order some food "
        context['data']=d
        context['data1']=p
        return render(request,'placeorder.html',context)
    
    return render(request,'placeorder.html',context)

def makepayment(request):

    d=User.objects.filter(username=request.user.username)
    p=customer_details.objects.filter(uname=request.user.username)
    context={}
    context['data']=d
    context['data1']=p


    userid=request.user.id
    carts = cart_page.objects.filter(uid=userid)
    Orders=orderP.objects.filter(uid=request.user.id)
     
    context['item']=Orders
    np=len(Orders)
    s=0 
    for x in Orders:
        s=s+x.pid.rupess * x.qty
        context['total']=s
        context['n']=np

    if not orderP.objects.filter(uid=request.user.id).exists():
        context['errmsg']="Order page is Empty ,order some food "
        context['data']=d
        context['data1']=p
        return render(request,'pay.html',context)
    
    
    order_p_records = orderP.objects.filter(uid=request.user.id)
    for order in order_p_records:
        orderid=random.randrange(1000,9999)
        OrderConfirmed.objects.create(
            order_id=orderid,
            pid=order.pid,
            uid=order.uid,
            qty=order.qty,
            rupess=s

        )
    oid=str(orderid)
    client = razorpay.Client(auth=("rzp_test_ntdeDahfUDEpdw", "wiff7Hem3hEdL4qEJZy0WEpU"))

    data = { "amount": s*100, "currency": "INR", "receipt": oid }
    payment = client.order.create(data=data)
    
    context['datad']=payment
    uemail=request.user.email
    uid=request.user.id
    
    context['uemail']=uemail
    context['uid']=uid
    # return HttpResponse("in makepayment section")
    return render(request,'pay.html',context)

def sendusermail(request,uemail,uid):
    # uemail=request.user.email
    carts = cart_page.objects.filter(uid=uid)
    s=0
    for x in carts:
            s=s+x.fid.rupess * x.qty
            
    order_conf = orderP.objects.filter(uid=uid)
    info = ""  
    for order in order_conf:
        foodname=order.pid.foodname
        cat=order.pid.food
        rupess=order.rupess
        Qty=order.qty
        if cat == 1:
            cate="Veg"
        else:
            cate="Non Veg"

        info += f"Food Name: {foodname}\nCategory: {cate}\nPrice: {rupess}\nQuantity: {Qty}  \nOrder Done\n \n"

    info += f"Total Rupess:{s}"
    context={}
    try:
        send_mail(
            "Food-order placed successfully",
            info,
            "shivamparab.sp@gmail.com",
            [uemail],
            fail_silently=False,
        )
        context['success_message'] = "Food-order placed successfully!"
    except Exception as e:
        context['success_message'] = f"Error sending mail: {str(e)}"
    
    
    order_p_records = orderP.objects.filter(uid=uid)    

   
    cart_page.objects.filter(uid=uid).delete()
    order_p_records.delete()
    
    
    
    return render(request,'index.html',context)


def OrderH(request):
    userid=request.user.id
    c=OrderConfirmed.objects.filter(uid=userid)
    context={}
    context['data']=c
    return render(request,'order_history.html',context)