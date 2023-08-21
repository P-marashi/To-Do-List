from django.contrib import admin
from django.urls import path, include

# URL patterns for the project
urlpatterns = [
    # Admin interface URL
    path('admin/', admin.site.urls),
    
    # Debug toolbar URL (for development)
    path("__debug__/", include("debug_toolbar.urls")),
    
    # Include user app's URL patterns
    path('', include('td_apps.user.urls')),
]