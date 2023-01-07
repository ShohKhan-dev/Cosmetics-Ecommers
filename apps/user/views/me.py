# Rest-Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Project
from user.serializers.me import UserMeSerializer


class UserMeAPIVIew(APIView):
    serializers_class = UserMeSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        context = {'request': request}
        serializer = self.serializers_class(request.user, context=context)
        return Response(data=serializer.data)

    def patch(self, request):
        context = {'request': request}
        serializer = self.serializers_class(request.user, data=request.data, partial=True, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
