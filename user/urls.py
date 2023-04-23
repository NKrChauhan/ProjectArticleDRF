from django.urls import path

from .views.user import UserView

urlpatterns = [
    path('', UserView.as_view(), name='user_view'),
]
