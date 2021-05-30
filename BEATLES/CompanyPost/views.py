from django.shortcuts import render,redirect
from django.http import HttpResponse
from CompanyPost.models import PostsInfo , PostComment,HandleSignUp
from django.contrib import messages

from django.core.paginator import Paginator ,EmptyPage ,PageNotAnInteger

# Create your views here.
def posthome(request):
    allposts = list(PostsInfo.objects.all())
    allposts.reverse()
    num=0
    for i in allposts:
        num+=1

    posts =  Paginator(allposts,3)
    page_num = request.GET.get('page')

    try:
        allposts = posts.page(page_num)
    except PageNotAnInteger:
        allposts = posts.page(1)
    except  EmptyPage:
        messages.warning(request,"Page Number Out of range")
        allposts = posts.page(posts.num_pages)

    context = {'allposts':allposts,'num':num}
    print(allposts)
    return render(request,'companyposts/posthome.html',context)

def postcontent(request,slug):
    # posts = PostsInfo.objects.filter(slug=slug) 
    # context = {'posts':posts}
    slug_post = PostsInfo.objects.filter(slug=slug)
    comments = list(PostComment.objects.filter(post__in=slug_post))
    comments.reverse()
    user = request.user
    hsu = HandleSignUp.objects.filter(username=user)
    #  = hsu.profile_pic
    context={'slug_post':slug_post,'comments':comments,'hsu':hsu}
    
    return render(request,'companyposts/postcontent.html',context)

def postComments(request):

    if request.method=='POST':
        
        comment = request.POST.get("comment")
        user = request.user
        
        postSno = request.POST.get("postSno")
        post = PostsInfo.objects.get(sno=postSno)
        newcomment  = PostComment(comment=comment,user=user,post=post)
        newcomment.save()
        messages.success(request,"Comment Postedccessfully")
        return redirect(f"/posts/{post.slug}")

    else:
        messages.warning(request,"Nhi hua comment")
        return redirect('home')