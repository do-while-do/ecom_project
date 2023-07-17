from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.inclusion_tag('core/tags/js_scripts_footer.html', name='js_scripts_footer')
def js_scripts_footer():
    # Perform any necessary logic or retrieve data here
    data = {'foo': 'bar'}
    return {'data': data}
