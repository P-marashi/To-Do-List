from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils.translation import gettext as _

from rest_framework import serializers

# Custom validator for One-Time-Pin (OTP) codes
class OTPCodeValidator:
    """
    Custom validator for One-Time-Pin (OTP) codes.
    
    This validator ensures that an OTP code is numeric and has a length of 5 characters.
    If the validation fails, it raises a serializers.ValidationError.
    """
    message = _("The OTP code should be numeric and have a length of 5 characters.")

    def __init__(self, message=None):
        self.message = message or self.message

    def __call__(self, attrs):
        code = str(attrs['code'])
        if len(code) != 5 or not code.isdigit():
            raise serializers.ValidationError(self.message, code="otp_invalid")

    def __repr__(self):
        return f"<{self.__class__.__name__}(message='{self.message}')>"

def password_match_checker(password, password_confirm):
    """
    Check if two password strings match.
    
    Args:
        password (str): The first password.
        password_confirm (str): The second password for confirmation.

    Returns:
        bool: True if the passwords match.

    Raises:
        serializers.ValidationError: If the passwords don't match.
    """
    if password != password_confirm:
        raise serializers.ValidationError(_("Passwords do not match"))
    return True

def check_user_existence(email):
    """
    Check if a user with the given email exists and is active.

    Args:
        email (str): The user's email.

    Returns:
        bool: True if the user exists and is active, False otherwise.
    """
    try:
        user = get_user_model().objects.values("is_active").get(
            Q(email=email)
        )
        return user['is_active']
    except get_user_model().DoesNotExist:
        return False
