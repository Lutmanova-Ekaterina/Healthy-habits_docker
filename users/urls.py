from django.urls import path


from users.views import UserCreateAPIView

urlpatterns = [
    path('user_create/', UserCreateAPIView.as_view()),
]
