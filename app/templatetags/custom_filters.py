from django import template
from urllib.parse import urlparse, urlsplit

register = template.Library()

@register.filter
def split_path(value):
    return urlparse(value).path.split('/')

@register.filter(name='isdigit')
def isdigit(value):
    return value.isdigit()

@register.filter(name='urlsplit')
def urlsplit_filter(value):
    return urlparse(value).path.split('/')

@register.filter
def urlparse_filter(value):
    return urlparse(value)