from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken

class EmailAuthentication:
    @staticmethod
    def authenticate(email: str, password: str):
        """
        Authenticate the user using email and password.
        Returns the authenticated user or None if authentication fails.
        """
        try:
            user = get_user_model().objects.get(Q(email=email))
        except get_user_model().DoesNotExist:
            return None

        if user and user.check_password(password):
            return user

        return None

    @staticmethod
    def generate_token(user):
        """
        Generate JWT tokens for the given user.
        Returns a dictionary containing 'refresh' and 'access' tokens.
        """
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    @staticmethod
    def blacklist_token(refresh_token):
        """
        Blacklist the given refresh token.
        Returns True if the token was successfully blacklisted.
        """
        token = RefreshToken(refresh_token)
        token.blacklist()
        return True

# Declare an instance of your custom authentication backend for easy access
email_authentication = EmailAuthentication()
