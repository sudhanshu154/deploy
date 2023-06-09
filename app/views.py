from types import FrameType
from django import forms
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from.models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        shoes = Product.objects.filter(category='S')
        laptop = Product.objects.filter(category='L')
        return render(request, 'app/home.html',{
            'topwears': topwears,
            'bottomwears': bottomwears,
            'mobiles': mobiles,
            'shoes': shoes,
            'laptop':laptop,
        })



#def home(request):
#return render(request, 'app/home.html')

#def product_detail(request):
# return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(selp, request, pk):
        product =  Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id)& Q(user=request.user)).exists()
        return render(request,'app/productdetail.html',{
            'product': product,'item_already_in_cart':item_already_in_cart})

@login_required
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')


def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required
def address(request):
    add= Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn primary'})

@login_required
def orders(request):
    op= OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'order_placed':op})



def mobile(request, data=None):
    if data == None:
        mobiles=Product.objects.filter(category='M')
    
    elif data =='below':
        mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=10000)
    elif data =='above':
        mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=10000)
    elif data == 'REDMI' or 'SAMSUNG':
        mobiles=Product.objects.filter(category='M').filter(brand=data)
    return render(request, 'app/mobile.html',{
        'mobiles':mobiles
    })

def SHOES(request, data=None):
    if data == None:
        SHOESs=Product.objects.filter(category='S')
    elif data =='below':
        SHOESs=Product.objects.filter(category='S').filter(discounted_price__lt=10000)
    elif data =='above':
        SHOESs=Product.objects.filter(category='S').filter(discounted_price__gt=12999)
    return render(request, 'app/SHOES.html',{
        'SHOESs':SHOESs
    })

def LAPTOP(request, data=None):
    if data == None:
        LAPTOPs=Product.objects.filter(category='L')
    elif data =='below':
        LAPTOPs=Product.objects.filter(category='L').filter(discounted_price__lt=10000)
    elif data =='above':
        LAPTOPs=Product.objects.filter(category='L').filter(discounted_price__gt=10000)
    return render(request, 'app/LAPTOP.html',{
        'LAPTOPs':LAPTOPs
    })

def TOPWEAR(request, data=None):
    if data == None:
        TOPWEARs=Product.objects.filter(category='TW')
    elif data =='below':
        TOPWEARs=Product.objects.filter(category='TW').filter(discounted_price__lt=10000)
    elif data =='above':
        TOPWEARs=Product.objects.filter(category='TW').filter(discounted_price__gt=10000)
    return render(request, 'app/TOPWEAR.html',{
        'TOPWEARs':TOPWEARs
    })

def BOTTOMWEAR(request, data=None):
    if data == None:
        BOTTOMWEARs=Product.objects.filter(category='BW')
    elif data =='below':
        BOTTOMWEARs=Product.objects.filter(category='BW').filter(discounted_price__lt=10000)
    elif data =='above':
        BOTTOMWEARs=Product.objects.filter(category='BW').filter(discounted_price__gt=12999)
    return render(request, 'app/BOTTOMWEAR.html',{
        'BOTTOMWEARs':BOTTOMWEARs
    })



class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{
            'form':form
        })
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request,'app/customerregistration.html',{
            'form':form
        })


def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items= Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    totalamount= 0.0
    cart_product=[p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
        totalamount=amount + shipping_amount
        return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items':cart_items})


@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self, request):
        form= CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form,'active':'btn-primary'})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user= usr,name=name, locality=locality,city=city,state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations !! Profile Updated Successfully')
        return render(request,'app/profile.html', {'form':form})

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount= 0.0
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user ==user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount= amount+shipping_amount
            return render(request, 'app/addtocart.html', {'carts':cart,'totalamount':totalamount,'amount':amount})
        else:
            return render(request,'app/emptycart.html')


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c =Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount= 70.0
        cart_product=[p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount

        data={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount+shipping_amount
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c =Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount= 70.0
        cart_product=[p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount

        data={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount +shipping_amount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c =Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount= 70.0
        cart_product=[p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount

        data={
            'amount': amount,
            'totalamount': amount +shipping_amount
        }
        return JsonResponse(data)


def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer= Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer ,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect("orders")
