from django.contrib.auth.models import User
import facebook
import settings
from social.models import Friendship

__author__ = 'kidzik'

def add_new_friends(request):
    if request.user.is_anonymous() or request.user.id == 1 or request.user.get_profile() == None:
        return
    user = facebook.get_user_from_cookie(request.COOKIES, settings.FACEBOOK_API_KEY, settings.FACEBOOK_SECRET_KEY)
    if user:
        graph = facebook.GraphAPI(user["access_token"])
        friends = graph.get_connections("me", "friends")
        friends = friends["data"]
        ids = [friend['id'] for friend in friends]
        friends = User.objects.all().filter(facebookprofile__uid__in = ids)

        friends = friends.exclude(id__in = [fd.user2.id for fd in Friendship.objects.filter(user1=request.user)])
        for friend in friends:
            f,c = Friendship.objects.get_or_create(user1 = request.user, user2 = friend)
            f.save()

