from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ..services.user import UserService
from ..serializers.user import UserSerializer, UserUpdateSerializer


class UserView(APIView):
    authentication_classes = []
    permission_classes = []
    user_serializer = UserSerializer
    user_update_serializer = UserUpdateSerializer

    def post(self, request):
        """
        Create user or get token for the existing user with correct password
        """
        serialized_data = self.user_serializer(data=request.data)
        user_service = UserService()
        if(serialized_data.is_valid(raise_exception=True)):
            validated_data = serialized_data.validated_data
            user = user_service.get_user_by_email(user_email=validated_data.get("email"))
            status_code = None

            if not user:
                user = user_service.create_user(validated_data)
                status_code = status.HTTP_201_CREATED
            else:
                status_code = status.HTTP_200_OK
            
            user = authenticate(email=validated_data.get("email"), password=validated_data.get("password"))

            token, _ = user_service.get_token_for_user(user.id)
            return Response(data={"access_token": token.key}, status=status_code)

    def put(self, request):
        """
        Change password and get token for the user
        """
        serialized_data = self.user_update_serializer(data=request.data)
        user_service = UserService()
        if(serialized_data.is_valid(raise_exception=True)):
            validated_data = serialized_data.validated_data
            
            user = authenticate(email=validated_data.get("email"), password=validated_data.get("previous_password"))
            
            user = user_service.update_password(user.id, validated_data.get("password"))
            
            token, _ = user_service.get_token_for_user(user.id)
            return Response(data={"access_token": token.key}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        """
        Delete User
        """
        is_user_deleted = UserService().delete_user(request.user.id)
        if is_user_deleted:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
