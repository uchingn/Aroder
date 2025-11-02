import django
from django.shortcuts import render
from .models import*
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
from django.shortcuts import render, get_object_or_404

# Create your views here.
 # ///////////////////////////////  home  ///////////////////////////////////////////
def home(request):
    alldata = Product.objects.all()  

    if request.method == "POST":
        searchpro = request.POST.get('findingproduct')
        print(searchpro, "hello this here??")

        if searchpro:   
            alldata = Product.objects.filter(name__icontains=searchpro)

    context = {
        'alldata': alldata,
    }
    return render(request, "products/products.html", context)



def logout(request):
    
    return redirect('login') 

def dashboard(request):
    user_id = request.session.get('user_id')  # Get the logged-in user ID

    if not user_id:
        return redirect('login')  # If no user logged in, redirect to login

    user_profile = Registeracount.objects.get(id=user_id)

    return render(request, 'dashboard.html', {'user_profile': user_profile})

# ///////////////////////////////  home end ///////////////////////////////////////////
# ///////////////////////////////  user registar and login  ///////////////////////////////////////////
@login_required
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        profile_pic = request.FILES.get('profile_pic')  # If it's a file upload
        password=request.POST.get('password')
        user_type = request.POST.get("user_type", "customer") 

        data_stor = Registeracount.objects.create(
            name=name,
            contact=contact,
            address=address,
            profile_pic=profile_pic,
            password=password,
            user_type=user_type,
            
        )
        data_stor.save()

        
        messages.success(request, 'রেজিস্ট্রেশন সফল হয়েছে! এখন আপনি লগইন করতে পারেন।')
        return redirect('login')  
    return render(request, "usertype/logsingdata/registerform.html")

def admin_dashboard(request):
     
    return render(request, "homeAddmin/admindashboard.html")

def login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
       

        user = Registeracount.objects.filter(contact=phone, password=password).first()
        if user:
            # Save info in session
            request.session['user_id'] = user.id
            request.session['user_type'] = user.user_type

            messages.success(request, 'সফলভাবে লগইন হয়েছে!')

            # Redirect based on user type
            if user.user_type == "seller":
                return redirect('selsman')  # Make sure this URL name exists
            elif user.user_type == "customer":
                return redirect('newpage_forbuyer')  # Make sure this URL name exists
            elif user.user_type == "delivery_person":
                return HttpResponse("NO PAGE YET")
            else:
                return HttpResponse("Unknown user type")
        else:
            messages.error(request, 'ভুল মোবাইল নম্বর বা পাসওয়ার্ড। আবার চেষ্টা করুন।')
            return redirect('login')  # Redirect back to login page
    return render(request, "usertype/logsingdata/acount_login.html")

# def login(request):  
#     if request.method == "POST":
#         contact = request.POST.get("contact")
#         password = request.POST.get("password")

#         try:
#             user = Registeracount.objects.get(contact=contact, password=password)
#             request.session['user_id'] = user.id  # Store logged-in user ID
#             return redirect('dashboard')  # Redirect to profile/dashboard page
#         except Registeracount.DoesNotExist:
#             messages.error(request, "ভুল মোবাইল বা পাসওয়ার্ড!")
#             return redirect('login')

#     return render(request, "usertype/logsingdata/acount_login.html")
# ///////////////////////////////  user registar and login end ///////////////////////////////////////////

# ///////////////////////////////  user typee  ///////////////////////////////////////////
def selsman(request):
    user_profile=Registeracount.objects.all()
    context={
        'user_profile':user_profile,
    }
    return render(request, "usertype/selsfarmar/main_user_profile.html",context)
def newpage_forbuyer(request):
    
    return render(request, 'usertype/selsfarmar/newpage.html')

def buyers(request):
     
    return render(request, "usertype/buyer/buyer.html")
# ///////////////////////////////  user typee end ///////////////////////////////////////////
# ///////////////////////////////  product  ///////////////////////////////////////////
def product(request):
    allpopolerpro = Product.objects.all()
    imageslid = AddImageSlide.objects.all()
    context = {
        'allpopolerpro': allpopolerpro,
        'imageslid': imageslid,
    }
    return render(request, "products/products.html", context)


def list_populer_product(request):
    allpro_list = Product.objects.all()  # QuerySet of Product objects
    context = {
        'allpro_list': allpro_list, 
         
    }
    return render(request, "products/listpopulerpro.html", context)
 

def category_products(request):
     
     return render(request,"products/categoriwiseproduct.html")
 
 
def product_entry(request):
    if request.method=='POST':
        catagoris=request.POST.get('catagoris')
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        stock=request.POST.get('stock')
        unit = request.POST.get('unit')
        data_stor=Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            catagoris=catagoris,
            unit=unit,
        )
        data_stor.save()
    return render(request,"usertype/logsingdata/entry_product.html")

def buyproduct(request,id):
    products=Product.objects.get(id=id)
    
    context={
        'products':products,
    }
    return render(request,"products/buyproduct.html",context)

 