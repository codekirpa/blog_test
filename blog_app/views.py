from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from blog_app.models import*
from django.db.models import Q

# Create your views here.
def login(request):
    if request.method == "POST":
        entered_username = request.POST['username']
        entered_password = request.POST['password']

        user = auth.authenticate(username=entered_username, password=entered_password)
        print(user)
        if user is not None:
            auth.login(request, user)   # login method starts a cookie-based session for that particular user.
            return redirect("home")
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect("login")
    else:
        return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        entered_username = request.POST['username']
        entered_password = request.POST['password']

        
        
        
        if User.objects.filter(username=entered_username).exists():
            messages.info(request, "Username already exists")
            return redirect("/signup")

        new_user = User.objects.create_user(username=entered_username, password=entered_password)

        new_user.save()

        return redirect("login")
    else:
        return render(request, 'register.html')
    
@login_required(login_url="/login")
def home(request):
      return render(request,'home.html')
def fillup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        location=request.POST['location']
        hobby=request.POST['hobby']
        email_id=request.POST['email_id']
        phone_num=request.POST['phone_num']
        
        new_cust=Customer(first_name=first_name,last_name=last_name,location=location,hobby=hobby,
                          email_id=email_id,phone_num=phone_num)
                         
        new_cust.save()
        return redirect('blogspage')
    else:
        return render(request,'fillup.html')
    
    
def  blogspage(request):
    blog=Blog.objects.all()
    cat=Category.objects.all()
    return render(request,'blogspage.html',{'blog':blog,'cat':cat})
def  specific(request,pk):
    category=Category.objects.get(id=pk)
    # category=Category.objects.exclude(~Q(id=int(pk)))
    cat2=Category.objects.all()
    blog1=Blog.objects.filter(category=category)
    return render(request,'specific.html',{'blog1':blog1,'cat2':cat2})    


