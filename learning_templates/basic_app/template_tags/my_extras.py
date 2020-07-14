from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value, arg):
    """
    This cuts out all values of 'arg' from the string!
    """

    return value.replace(arg, '')

# register.filter('cut', cut) #first one is the name you want to call this function and second one is the function itself
