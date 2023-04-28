from django.shortcuts import render, redirect
from item.models import Category, Item,Cart, CartItem
from .forms import Signup
from django.http import HttpResponse, JsonResponse
import json

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



def cart(request):

    print("cart")

    cart = None
    cartitems=[]

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()
        print("this line is execurted")
        # cartItem.quantity += 1
        # cartItem.save()
        # print(cartItem)
        # print(cart)

    context = {"cart":cart, "items":cartitems}
    return render(request, 'cart.html', context)



def add_to_cart(request):
    print("add to cart")
    data = json.loads(request.body)
    productId = data["id"]
    product = Item.objects.get(id=productId)

    # return JsonResponse(request.user.is_authenticated, safe=False)
    # print(request.user.is_authenticated)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cartItem.quantity += 1
        cartItem.save()
        return JsonResponse(cartItem, safe=False)


    return JsonResponse("mdskmfclsdmfsdmkfv", safe=False)