from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.inclusion_tag('core/tags/footer_links.html', name='footer_links')
def footer_links():
    # Perform any necessary logic or retrieve data here
    data = {'foo': 'bar'}
    return {'data': data}
