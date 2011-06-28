from django.views.generic.simple import direct_to_template
from sweetrs.social import add_new_friends

__author__ = 'kidzik'

def social_friends(request):
    add_new_friends(request)

    return direct_to_template(request, 'flatpages/friends.html')
