from pipes import Template
from django.template import Library

register = Library()

def is_member(obj, current_user):
    return obj.is_member(current_user)

register.filter('is_member', is_member)