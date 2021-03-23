from django import template

register = template.Library()


@register.filter(name='blog_range')
def get_range(value):
    return [x for x in range(value)]