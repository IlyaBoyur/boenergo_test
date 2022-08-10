from django import template


register = template.Library()


@register.filter
def int_2_color(value):
    "Convert integer to template color"
    color = hex(value)[2:].upper()
    return '#' + '0' * (6 - len(color)) + color
