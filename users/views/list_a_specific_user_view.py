from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status

from users.models import User
from users.permissions import IsProfileOwner
from users.serializers.user_serializer import UserSerializer


class ListASpecificUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsProfileOwner]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)

        return Response(serializer.data)
