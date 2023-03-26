from django.shortcuts import render
from .models import Blog
from category.models import Category
from comment.forms import CommentForm
from django.shortcuts import redirect
from django.urls import reverse
from comment.models import Comment
from .filters import BlogFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def blog_list(request):
    blog_list=Blog.objects.all()

    myfilter=BlogFilter(request.GET,queryset=blog_list)
    blog_list=myfilter.qs

    paginator=Paginator(blog_list,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    

    post_popular=Blog.objects.order_by('created_at')[:3]
    category=Category.objects.all()
    
    context={'blogs':page_obj,'category':category,'post_popular':post_popular,'myfilter':myfilter}
    return render(request,'blog/blog_list.html',context)
    



def blog_details(request,blog_url):
    blog_title=blog_url.replace('-',' ')
    blog_detail=Blog.objects.get(title=blog_title)
    post_popular=Blog.objects.order_by('created_at')[:3]
    category=Category.objects.all()
    comment=Comment.objects.all()

    paginator=Paginator(comment,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user_id=request.user.id
            comment.post_id=blog_detail.id
            comment.save()
            return redirect(reverse('blog:blogdetail_page/<str:blog_url>'))
           
    else:
        form=CommentForm()

    context={'blog':blog_detail,'post_popular':post_popular,'category':category,'form':form,'comment':page_obj}
    return render(request,'blog/blog_detail.html',context)
    