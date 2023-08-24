from django.urls import path
from .apis import AuthViewSet

urlpatterns = [
    # URL pattern for user login
    path('auth/login/', AuthViewSet.as_view({'post': 'login'}), name='login'),

    # URL pattern for user registration
    path('auth/register/', AuthViewSet.as_view({'post': 'register'}), name='register'),

    path('auth/verify/<uidb64>/<token>/', AuthViewSet.as_view({'post': 'verify'}), name='register/verify'),
    
]