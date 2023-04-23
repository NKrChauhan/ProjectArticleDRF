from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token


User = get_user_model()

class UserService:
    def create_user(self, user_data):
        user = User(**user_data)
        user.save()
        return user

    def update_password(self, user_id, new_password):
        user = User.objects.filter(pk=user_id).first()
        user.password = new_password
        user.save()
        return user

    def delete_user(self, user_id):
        article = User.objects.get(pk=user_id)
        article.delete()
        return True

    def get_user_by_email(self, user_email):
        user = User.objects.filter(email=user_email)
        return user.first()
    
    def get_user_by_id(self, user_id):
        user = get_object_or_404(User, pk=user_id)
        return user
        
    def get_token_for_user(self, user_id):
        user = self.get_user_by_id(user_id=user_id)
        token, is_created = Token.objects.get_or_create(user=user)
        return token, is_created

