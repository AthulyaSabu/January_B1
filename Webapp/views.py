from django.shortcuts import render,redirect
from Backend.models import ProductDb,CategoryDB
from Webapp.models import ContactDb,RegisterDb,CartDb
from django.contrib import messages
# Create your views here.
def homepage(request):
    cat = CategoryDB.objects.all()
    return render(request, "Home.html", {'cat':cat})
def aboutpage(request):
    cat = CategoryDB.objects.all()
    return render(request, "about.html", {'cat':cat})
def our_products(request):
    pro = ProductDb.objects.all()
    cat = CategoryDB.objects.all()
    return render(request, "OurProducts.html", {'products':pro, 'cat':cat})
def filtered_products(request, cat_name):
    data = ProductDb.objects.filter(Category=cat_name)
    return render(request,"Products_Filtered.html", {'data':data})
def single_productpage(request, pro_id):
    data = ProductDb.objects.get(id=pro_id)
    cat = CategoryDB.objects.all()
    return render(request, "Single_Product.html",{'data':data, 'cat':cat})
def contactpage(request):
    cat = CategoryDB.objects.all()
    return render(request, "Contact.html",{'cat':cat})
def save_contact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        ph = request.POST.get('phone')
        obj = ContactDb(Name=na, Email=em, Subject=sub, Message=msg, Mobile=ph)
        obj.save()
        return redirect(contactpage)

def registration_page(req):
    return render(req,"Register.html")
def save_user(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        p1 = request.POST.get('pass1')
        p2 = request.POST.get('pass2')
        img = request.POST.get('image')
        obj = RegisterDb(Username=na, Email=em, Password=p1, ConfirmPassword=p2, ProfileImage=img)
        if RegisterDb.objects.filter(Username=na).exists():
            messages.warning(request, "Username already exists..!")
            return redirect(registration_page)
        elif RegisterDb.objects.filter(Email=em).exists():
            messages.warning(request, "Email id already exists..!")
            return redirect(registration_page)
        else:
            obj.save()
            messages.success(request, "Registered successfully..!")
        return redirect(registration_page)

def UserLogin(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pswd = request.POST.get('password')
        if RegisterDb.objects.filter(Username=un, Password=pswd).exists():
            request.session['Username']=un
            request.session['Password']=pswd
            return redirect(homepage)
        else:
            return redirect(registration_page)
    else:
        return redirect(registration_page)
def UserLogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(homepage)
def save_cart(request):
    if request.method == "POST":
        na = request.POST.get('username')
        pn = request.POST.get('productname')
        tot = request.POST.get('total')
        qty = request.POST.get('quantity')
        obj = CartDb(Username=na, ProductName=pn, Quantity=qty, TotalPrice=tot)
        obj.save()
        return redirect(homepage)

def cart_page(request):
    data = CartDb.objects.filter(Username=request.session['Username'])
    total = 0
    for d in data:
        total = total+d.TotalPrice
    return render(request,"Cart.html", {'data':data, 'total':total})

def delete_item(request, p_id):
    x = CartDb.objects.filter(id=p_id)
    x.delete()
    return redirect(cart_page)
def user_login_page(request):
    return render(request, "Userlogin.html")