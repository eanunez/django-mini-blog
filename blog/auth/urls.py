from django.urls import path
from auth.views import EmailTokenObtainPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup', RegisterView.as_view(), name='auth_signup'),
]