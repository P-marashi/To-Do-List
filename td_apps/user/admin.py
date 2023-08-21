from django.contrib import admin
from .models import User


# Customizing the UserAdmin interface for the User model
class UserAdmin(admin.ModelAdmin):
    # Display fields in the admin list view
    list_display = (
        "email",
        "is_active",
        "is_admin",
        "is_superuser",
        "created_at",
        "updated_at"
    )

    # Filter options in the right sidebar
    list_filter = (
        "is_active",
        "is_admin",
        "is_superuser",
        "created_at"
    )

    # Add a search bar to find users by email
    search_fields = ('email',)

    # Set the default ordering of the users in the list view
    ordering = ('-created_at',)

# Register the User model with the custom UserAdmin settings
admin.site.register(User, UserAdmin)
