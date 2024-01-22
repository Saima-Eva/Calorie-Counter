from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
from .models import UserProfile,ConsumedItems
from .forms import UserForm,SignInForm,UserProfileForm,ConsumedItemForm,DateForm

def home(request):
    user = request.user
    consumed_items = ConsumedItems.objects.filter(user=user)
    return render(request,'home.html',{'items':consumed_items})

def dailyrequired(request):
    user=request.user
    obj=0
    try:
        obj, created = UserProfile.objects.get_or_create(user=user)
        
    except:
        pass
    if obj:
        if obj.gender == 'Male':
            print(obj.gender)
            BMR=66.47+(13.75*obj.weight)+(5.003*obj.height)-(6.755*obj.age)
        else:
            BMR=655.1+(9.563*obj.weight)+(1.850*obj.height)-(4.676*obj.age)
        return BMR
    return 0
def calory_get(request,date,obj,user):
    consumed_items_today = ConsumedItems.objects.filter(user=user,created_at__date=date)
    sum=0
    for i in consumed_items_today:
        sum+=i.calories_consumed
    return sum 

def profile(request):
    user=request.user
    obj=0
    data=None
    calory=0
    need=None
    noneed=None
    consumed_items = ConsumedItems.objects.filter(user=user)
    try:
        obj, created = UserProfile.objects.get_or_create(user=user)
        
    except:
        pass
    BMR=dailyrequired(request)
    if request.method=="POST":
        data=request.POST.get('date')
        
        print(data)
        if obj:
            calory=calory_get(request,data,obj,user)
            need=BMR-calory
            if need <= 0:
                noneed=need
                
    
    
    return render(request,'profile.html',{'obj':obj,'user_d':user,'BMR':BMR,'data':data,'items':consumed_items,'calory':calory,'need':need,'noneed':noneed})


def user_profile_update(request):
    user=request.user
    user_instance = User.objects.get(id=user.id)
    obj=0
    
    
    try:
        obj, created = UserProfile.objects.get_or_create(user=user_instance)
        
    except:
        pass
    
    if request.method=="POST" and obj:
        form=UserProfileForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    elif request.method=="POST":
        form=UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.user=request.user
            form2.save()
            return redirect('home')
    

    elif obj:
        form=UserProfileForm(instance=obj)
    else:
        form=UserProfileForm()
    return render(request,"user_profile.html",{'form':form})

def consume_calories(request):
    
    if request.method=="POST":
        form=ConsumedItemForm(request.POST)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.user=request.user
            form2.save()
            return redirect('home')
    

    else:
        form=ConsumedItemForm()
    return render(request,"consume_calories.html",{'form':form})




def update_item(request,id):
    obj=ConsumedItems.objects.get(pk=id)
    if request.method=="POST":
        form=ConsumedItemForm(request.POST,instance=obj)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.user=request.user
            form2.save()
            return redirect('home')
    else:
        form=ConsumedItemForm(instance=obj)
    return render(request,"consume_calories.html",{'form':form})

def delete_item(request,id):
    obj=ConsumedItems.objects.get(pk=id)
    obj.delete()
    return redirect('home')




def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SignIn')
    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})

def SignIn(request):   
    if request.method=="POST":
        form=SignInForm(request.POST)
        if form.is_valid():
            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            if not user:
                messages.warning(request,'The User Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            if user:
                
                login(request, user)
                return redirect('home')
    else:
        form=SignInForm()
    return render(request,'login.html',{'form':form})

def logout_f(request):
    logout(request)
    return redirect('SignIn')