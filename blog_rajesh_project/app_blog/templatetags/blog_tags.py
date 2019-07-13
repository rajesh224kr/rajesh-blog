from app_blog.models import Post
from django import template
register=template.Library()


#utility function to define custom template tages

#@register.simple_tag(name='my_tag') >>>>base.html also change total_tag=my_tag
@register.simple_tag
def total_post():
    return Post.objects.count()

#usage of inclusion_tag to disply LATEST POST

@register.inclusion_tag('blog/least_post123.html')
def show_least_posts(count=4):
    least_post=Post.objects.order_by('-publish')[:count]
    return {'least_post':least_post}
#usage of assignment tag to display most comment posts
