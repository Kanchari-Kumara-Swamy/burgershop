from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *


# Create your views here.
def adminloginview(request):
    return render(request, "burger_shop/adminlogin.html")


def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    # user exists
    if user is not None:
        login(request, user)
        return redirect('adminhomepage')

    # user doesnt exists
    if user is None:
        messages.add_message(request, messages.ERROR, "invalid credentials")
        return redirect('adminloginpage')


def adminhomepageview(request):
    context = {'burgers': BurgerModel.objects.all()}
    return render(request, "burger_shop/adminhomepage.html", context)


def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')


def addburger(request):
    # write a code to add the burger into the database
    name = request.POST['burger']
    price = request.POST['price']
    BurgerModel(name=name, price=price).save()
    return redirect('adminhomepage')


def deleteburger(request, pk):
    BurgerModel.objects.filter(id = pk).delete()
    return redirect('adminhomepage')


def homepageview(request):
    return render(request, "burger_shop/homepage.html")


def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phoneno']
    # if username already exists
    if User.objects.filter(username=username).exists():
        messages.add_message(request, messages.ERROR, "user already exists")
        return redirect('homepage')
    # if username doesnt exist already(everything is fine to create user)
    User.objects.create_user(username=username, password=password).save()
    lastobject = len(User.objects.all()) - 1
    CustomerModel(userid=User.objects.all()[int(lastobject)].id, phoneno=phoneno).save()
    messages.add_message(request, messages.ERROR, "user succesfully created")
    return redirect('homepage')


def userloginview(request):
    return render(request, "burger_shop/userlogin.html")


def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    # user exists
    if user is not None:
        login(request, user)
        return redirect('customerpage')

    # user doesnt exists
    if user is None:
        messages.add_message(request, messages.ERROR, "invalid credentials")
        return redirect('userloginpage')


def customerwelcomeview(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')

    username = request.user.username
    context = {'username': username, 'burgers': BurgerModel.objects.all()}
    return render(request, 'burger_shop/customerpage.html', context)


def userlogout(request):
    logout(request)

    return redirect('userloginpage')


def placeorder(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')

    username = request.user.username
    phoneno = CustomerModel.objects.filter(userid=request.user.id)[0].phoneno
    address = request.POST['address']
    ordereditems = ""
    for burger in BurgerModel.objects.all():
        burgerid = burger.id
        name = burger.name
        price = burger.price

        quantity = request.POST.get(str(burgerid), " ")

        if str(quantity) != "0" and str(quantity) != " ":
            ordereditems = ordereditems + name + " " + "price : " + str(
                int(quantity) * int(price)) + " " + "quantity : " + quantity + "    "

    print(ordereditems)

    OrderModel(username=username, phoneno=phoneno, address=address, ordereditems=ordereditems).save()
    messages.add_message(request, messages.ERROR, "order succesfully placed")
    return redirect('customerpage')


def userorders(request):
    orders = OrderModel.objects.filter(username=request.user.username)
    context = {'orders': orders}
    return render(request, 'burger_shop/userorders.html', context)


def adminorders(request):
    orders = OrderModel.objects.all()
    context = {'orders': orders}
    return render(request, 'burger_shop/adminorders.html', context)


def acceptorder(request, orderpk):
    order = OrderModel.objects.filter(id=orderpk)[0]
    order.status = "accepted"
    order.save()
    return redirect(request.META['HTTP_REFERER'])


def declineorder(request, orderpk):
    order = OrderModel.objects.filter(id=orderpk)[0]
    order.status = "declined"
    order.save()
    return redirect(request.META['HTTP_REFERER'])


