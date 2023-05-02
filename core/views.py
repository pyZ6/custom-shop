from django.shortcuts import render, redirect
from item.models import Category, Item,Cart, CartItem
from .forms import Signup
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
def index(request):
    items = Item.objects.filter(is_sold = False)[0:100]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories': categories,
        'Items': items,
    })
def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:    
        form = Signup()
    return render(request, 'core/signup.html',{
        'form':form
    })

def say_hello(request):
    text = """dear User :) Welcome to OODY Custom shop"""
    return render(request, 'core/sayhello.html')


@login_required
def cart(request):
    my_integer = 0
    print("cart")
    cart = None
    cartitems=[]
    pricelist = []
    namelist = []
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()
        
        for i in cartitems:
            j = str(i)
            namelist.append(j)
        # for i in namelist:
        #     print(i)
        # print(namelist)
        sum = 0
        basket = Item.objects.filter(name__in=namelist)
        for i in basket:
            print("i.quantity => "+str(i.quantity))
            x= i.price * i.quantity
            sum = sum + x

        my_integer = len(namelist)
        print("this line is execurted")
        # cartItem.quantity += 1
        # cartItem.save()
        # print(cartItem)
        # print(cart)
    context = {"cart":cart, "items":cartitems, "pricelist":pricelist, "Basket":basket, "my_integer":my_integer,"sum":sum}
    return render(request, 'cart.html', context)


@login_required
def add_to_cart(request):
    print("add to cart")
    data = json.loads(request.body)
    productId = data["id"]
    prices = list()
    product = Item.objects.get(id=productId)
    print()

    # return JsonResponse(request.user.is_authenticated, safe=False)
    # print(request.user.is_authenticated)

    if request.user.is_authenticated:
        product.quantity += 1
        # print(product)
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        # cartItem.quantity += 1
        cartItem.save()
        return JsonResponse(cartItem, safe=False)


    return JsonResponse("mdskmfclsdmfsdmkfv", safe=False)