from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.inclusion_tag('core/tags/head_css.html', name='head_css')
def render_head_css():
    # Perform any necessary logic or retrieve data here
    data = {'foo': 'bar'}
    return {'data': data}
