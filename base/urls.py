from django.urls import path
from .views import  CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='custom_login'),
    path('refresh/', TokenRefreshView.as_view(), name="token_referesh")
]
