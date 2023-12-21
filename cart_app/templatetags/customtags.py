from django import template
register=template.Library()


@register.filter('product')
def product(value):
    return (type(value),value)

@register.filter('adding')
def adding(value,value1):
    return int(float(value))*int(float(value1))
