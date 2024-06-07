from django.shortcuts import render,redirect
from Backend.models import CategoryDB,ProductDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.
def indexpage(request):
    return render(request, "index.html")
def category_page(req):
    return render(req, "Category.html")
def save_category(request):
    if request.method == "POST":
        cn = request.POST.get('cname')
        des = request.POST.get('description')
        img = request.FILES['cimage']
        obj = CategoryDB(CategoryName=cn, Description=des, CategoryImage=img)
        obj.save()
        messages.error(request, "Category saved successfully..!")
        return redirect(category_page)
def category_display(req):
    data = CategoryDB.objects.all()
    return render(req, "Category_Display.html", {'data':data})
def category_edit(req, cat_id):
    data = CategoryDB.objects.get(id=cat_id)
    return render(req, "Edit_Category.html", {'data':data})

def UpdateCategory(request, cat_id):
    if request.method=="POST":
        cat = request.POST.get('cname')
        des = request.POST.get('description')
        try:
            img = request.FILES['cimage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=cat_id).CategoryImage
        CategoryDB.objects.filter(id=cat_id).update(CategoryName=cat, Description=des, CategoryImage=file)
        return redirect(category_display)
def DeleteCategory(request,cat_id):
    data = CategoryDB.objects.filter(id=cat_id)
    data.delete()
    messages.error(request, "Deleted..!")
    return redirect(category_display)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
def admin_page(req):
    return render(req, "Adminlogin.html")

def Admin_Login(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pwd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request, "Welcome..!")
                return redirect(indexpage)
            else:
                messages.error(request,"Invalid password..!")
                return redirect(admin_page)
        else:
            messages.warning(request, "User not found..!")
            return redirect(admin_page)


def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_page)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
def product_page(req):
    cat = CategoryDB.objects.all()
    return render(req, "Products.html", {'cat':cat})
def save_product(request):
    if request.method == "POST":
        cn = request.POST.get('cname')
        pn = request.POST.get('pname')
        pr = request.POST.get('price')
        des = request.POST.get('description')
        img = request.FILES['pimage']
        obj = ProductDb(Category=cn,ProductName=pn, Price=pr, Description=des, ProductImage=img)
        obj.save()
        return redirect(product_page)
def display_product_page(req):
    pro = ProductDb.objects.all()
    return render(req, "Product_Display.html", {'pro':pro})
def product_edit(req, pro_id):
    pro = ProductDb.objects.get(id=pro_id)
    cat = CategoryDB.objects.all()
    return render(req, "Edit_Product.html", {'pro':pro,'cat':cat})


