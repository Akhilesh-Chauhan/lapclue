from django.shortcuts import render,redirect
from lap.models import SignUp, AcountDetails, AllProducts, Cart
from .forms import ProductForm
import os

# Create your views here.
def index(request):
    prod=AllProducts.objects.all()
    context={'prod':prod}
    return render(request,'index.html',context)
    
def login(request):
    if request.method=='POST':
        try:
            UserDetails=SignUp.objects.get(email=request.POST['email'],password=request.POST['password'])
            request.session['name']=UserDetails.name
            request.session['email']=UserDetails.email
            if UserDetails.atype=='admin':
                request.session['atype']=UserDetails.atype
            return render(request,'index.html')
        except:
            return render(request,'login.html')
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        name=request.POST.get('username')
        phoneno=request.POST.get('phoneno')
        email=request.POST.get('email')
        password=request.POST.get('password')
        signup=SignUp(name,phoneno,email,password)
        signup.save()
        return render(request,'login.html')
    return render(request,'signup.html')

def profile(request,pk):
    profile=AcountDetails.objects.filter(email=pk)
    context={'profile':profile}
    return render(request,'profile.html',context)

def editprofile(request,pk):
    profile=AcountDetails.objects.get(email=pk)
    if request.method=='POST':
        if len(request.FILES)!=0:
            if len(profile.image)>0:
                os.remove(profile.image.path)
                profile.image=request.FILES['image']
        profile.name=request.POST['name']
        profile.email=request.POST['email']
        profile.phoneno=request.POST['phoneno']
        profile.dateofbirth=request.POST['dateofbirth']
        profile.gender=request.POST['gender']
        profile.address=request.POST['address']
        profile.pincode=request.POST['pincode']
        profile.save()
        return redirect('/profile')
    context={'profile': profile}
    return render(request,'editprofile.html',context)

def logout(request):
    try:
        del request.session['name']
        del request.session['atype']
    except:
        return render(request,'login.html')
    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

def companies(request):
    return render(request,'companies.html')

def addproduct(request):
    form=ProductForm(request.POST, request.FILES)        
    if request.method=='POST':
        if form.is_valid():
            form.save() 
            prd_obj=form.instance
            return render(request,'addproduct.html',{'form': form,'prd_obj':prd_obj})  
        else:
            form=ProductForm()      
    return render(request,'addproduct.html',{'form':form})

def products(request,category):
    if category=='all':
        prod=AllProducts.objects.all()
        context={'prod':prod}
        return render(request,'products.html',context)
    else:
        prod=AllProducts.objects.filter(category=category)
        context={'prod':prod}
        return render(request,'products.html',context)

def productdetails(request,pk):    
    try:
        details=AllProducts.objects.filter(id=pk)
        context={'details':details}
        return render(request,'productdetails.html',context)
    except:
        return render(request,'products.html')

def cart(request,code):
    item=AllProducts.objects.get(id=code)
    cart=Cart()
    cart.cname=item.cname
    cart.category=item.category
    cart.price=item.price
    cart.modelno=item.modelno
    cart.description=item.description
    cart.id=item.id
    cart.image=item.image
    cart.save()
    # Rendering the cart page
    items=Cart.objects.all()
    product=[]
    for i in items:
        if i.status=='unordered':
            product.append(i) 
    p1=[]
    p2=[]
    for count,i in enumerate(product):
        if count>(len(product)//2)+1:
            p1.append(i)
        else:
            p2.append(i)
    l=len(product)
    return render(request,'cart.html',{'item1':p1,'item2':p2,'lenght':l})



def cart_display(request):
    items=Cart.objects.all()
    product=[]
    for i in items:
        if i.status=='unordered':
            product.append(i)  
    p1=[]
    p2=[]
    for count,i in enumerate(product):
        if count>(len(product)//2)+1:
            p1.append(i)
        else:
            p2.append(i)
    l=len(product)
    return render(request,'cart.html',{'item1':p1,'item2':p2,'lenght':l})

def order(request,code):
    item=Cart.objects.get(id=code)
    item.status='ordered'
    item.save()
    product=AllProducts.objects.get(id=code)
    product.quantity-=item.quantity
    product.save()
    # Rendering the orders page
    items=Cart.objects.all()
    product=[]
    for i in items:
        if i.status=='ordered':
            product.append(i)
    p1=[]
    p2=[]
    for count,i in enumerate(product):
        if count>(len(product)//2)+1:
            p1.append(i)
        else:
            p2.append(i)
    l=len(product)
    return render(request,'order.html',{'item1':p1,'item2':p2,'lenght':l})

def order_display(request):
    items=Cart.objects.all()
    product=[]
    for i in items:
        if i.status=='ordered':
            product.append(i)
    p1=[]
    p2=[]
    for count,i in enumerate(product):
        if count>(len(product)//2)+1:
            p1.append(i)
        else:
            p2.append(i)
    l=len(product)
    return render(request,'order.html',{'item1':p1,'item2':p2,'lenght':l})

def cancel(request,code):
    item=Cart.objects.get(id=code)
    item.delete()
    items=Cart.objects.all()
    product=[]
    for i in items:
        if i.status=='unordered':
            product.append(i)  
    p1=[]
    p2=[]
    for count,i in enumerate(product):
        if count>(len(product)//2)+1:
            p1.append(i)
        else:
            p2.append(i)
    l=len(product)
    return render(request,'cart.html',{'item1':p1,'item2':p2,'lenght':l})
  
