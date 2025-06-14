from django import template

register = template.Library()


@register.filter
def multiply(value, arg):
    """將兩個數相乘"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ""
