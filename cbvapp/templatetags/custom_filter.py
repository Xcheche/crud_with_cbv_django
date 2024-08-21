from django import template

register = template.Library()
def custLower(value):
    #result = value[::].lower()       or do this
    result = value.lower()
    return result



register.filter('myLower', custLower)

#Using a decorator
@register.filter(name='myLove')
def mycustLower(value):
     
    result = value.lower()
    return result

 # Passing Arguments/Parameters
@register.filter(name='myAppend')
def customAppend(value, arg):
    # Concatenate the argument and the original value
    return str(arg) + str(value)

