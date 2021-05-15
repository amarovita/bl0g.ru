from django import template
from posts.models import Post

register = template.Library()

@register.simple_tag(takes_context=True)
def load_latest_posts(context):
    context['latest_posts'] = Post.objects.filter(published=True)[:10] 
    return ''
