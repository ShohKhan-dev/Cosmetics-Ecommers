import instaloader
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from instaloader import Instaloader, Profile
#
# L = Instaloader()
# L.login("Q8459S", "mtiFUUbUAa49syi")
# USERNAME = "onmacabim.de"


class InstagramPosts(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        result = []
        # profile = Profile.from_username(L.context, USERNAME)
        # photos = iter(profile.get_posts())
        # for _ in range(10):
        #     photo = next(photos)
        #     result.append({
        #         "url": photo.url,
        #         "likes": photo.likes,
        #         "comments": photo.comments,
        #         "caption": photo.caption,
        #     })
        return Response(result)
