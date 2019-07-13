from django.shortcuts import render,get_object_or_404
from app_blog.models import Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
from app_blog.forms import CommentForm
def post_list_view(request):
    post_list=Post.objects.all()
    #Tag qry


    #paginatior qry
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=Paginator.page(Paginator.num_pages)

    return render(request,'blog/post_list.html',{'post_list':post_list})

# from django.views.generic import ListView
# class Post_List_View(ListView):
#     model = Post
#     paginate_by = 2


def post_detail_view(request,year,month,day,post):
    try:
        post=get_object_or_404(Post,slug=post ,status='published',
                               publish_year=year,
                               publish_month=month,
                               publish_day=day) #get_object_or_404 it is a shortcut for object is available then display
        return render(request,'blog/post_detail.html',{'post':post})
    except:
        post = get_object_or_404(Post, slug=post, status='published')

    #comment section
        comments=post.comments.filter(active=True)
        csubmit=False
        if request.method=="POST":
            form=CommentForm(request.POST)
            if form.is_valid():
                new_comments=form.save(commit=False)
                new_comments.post=post
                new_comments.save()
                csubmit=True
        else:
            form=CommentForm()
        return render(request,'blog/post_detail.html',{'post':post,'comments':comments,'form':form,'csubmit':csubmit})

#email configurations
# from django.core.mail import send_mail
# from  app_blog.forms import EmailSendForm
# def mail_sned_view(request,id):
#     post=get_object_or_404(Post,id=id,status='published')
#     sent=False
#     if request.method=="POST":
#         form=EmailSendForm(request.POST)
#         if form.is_valid():
#             cd=form.cleaned_data
#             send_mail('subject','message','rajesh@gmail.com',[cd['to_mail']])
#             sent=True
#     else:
#         form=EmailSendForm()
#     return render(request,'blog/sharebymail.html',{'post':post,"form":form,'sent':sent})
from django.core.mail import send_mail
from  app_blog.forms import EmailSendForm
def mail_sned_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=="POST":
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({}) recommend you to read "{}"'.format(cd['name'],cd['form_mail'],post.title)
            post_url=request.build_absolute_uri(post.get_absolute_url() )
            message='Read Post At :\n {} \n\n {}\'s Comments :\n{} \n{}'.format(post_url,cd['name'],cd['comments'],cd['city'])
            send_mail(subject,message,'rajesh@gmail.com',[cd['to_mail']])
            sent=True
    else:
        form=EmailSendForm()
    return render(request,'blog/sharebymail.html',{'post':post,"form":form,'sent':sent})



