from django.shortcuts import render,redirect
from django.contrib import messages
from HOME.models import Contact 
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CompanyPost.models import PostsInfo , HandleSignUp,PostComment
from django.db import IntegrityError
# Create your views here.
# HTML TEMPLATES
def home(request):
    latest_post = list(PostsInfo.objects.all())
    latest_post.reverse()
    context={'latest_post':latest_post[:1]}
    return render(request,'home/home.html',context)

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)>3 and len(content)>5:
            contact = Contact(name=name,phone=phone,email=email,content=content)
            contact.save() 
            messages.success(request,"Successfully Form Filled ")
            print(name,email,phone,content)
        else:
            messages.warning(request,"Form Not Submitted\nPlease Fill it Again..")

    return render(request,'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query)==0:
        messages.warning(request,"Enter some query")
        return render(request,'home/search.html')
    else:    
    # allPosts = list(PostsInfo.objects.filter())
        allPosts = list(PostsInfo.objects.filter(title__icontains=query))
        allPosts.reverse()
        params = {'allPosts':allPosts}
        return render(request,'home/search.html',params)

# Authentication API's
def handleSignup(request):
    if request.method=='POST':
        try:
            username = request.POST['username']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            pass1 = request.POST['password']
            pass2 = request.POST['verifypassword']
            if pass1==pass2 and len(username)>4 :
                if not username.isalnum():
                    print("INSIDE ALNUM")
                    messages.warning(request,"UserName Must be AlphaNumeric Try Again")
                    return redirect('home')
                else:
                    acc_details = HandleSignUp(username=username,first_name=fname,last_name=lname,email=email,password=pass1)
                    acc_details.save()
                    myuser = User.objects.create_user(username,email,pass1)
                    myuser.first_name = fname
                    myuser.last_name = lname
                    myuser.save()
                    messages.success(request,"BEATLES Account Created ")
                    return redirect('home')
                
            
            elif pass1!=pass2 :
                messages.warning(request,'Wrong Password')
                return redirect('home')
        except IntegrityError as e: 
            # if 'unique constraint' in e.User:
            #     # duplicate detected
            messages.info(request,"Already registred Username")
            return redirect('home')
    else:
        return HttpResponse("404 - Error Not Found")

def handleLogin(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']    
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('home')
        else:
            messages.warning(request,"Wrong Credentials")
            return redirect('home')

    return HttpResponse("Login")

def handleLogOut(request):
    
    logout(request)
    messages.success(request,"Logged Out")
    return redirect('home')
    

# def postcomments(request):
#     if request.method=='POST':
#         messages.success(request,'YOHO')
#         return redirect('home')
#         comment = request.POST.get("comment")
#         user = request.user
#         postSno = request.POST.get("postSno")
#         post = PostsInfo.objects.get(sno=postSno)

#         comment  = PostComment(comment=comment,user=user,post=post)
#         comment.save()
#         messages.success(request,"Comment Postedccessfully")
    
#     return redirect(f"posts/{post.slug}")