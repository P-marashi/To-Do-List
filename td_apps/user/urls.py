from django.urls import path
from .apis import AuthViewSet

urlpatterns = [
    # URL pattern for user login
    path('auth/login/', AuthViewSet.as_view({'post': 'login'}), name='login'),

    # URL pattern for user registration
    path('auth/register/', AuthViewSet.as_view({'post': 'register'}), name='register'),
]
