from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from rest_framework import serializers
from td_apps.core.cache import get_cached_otp
from td_apps.core import validator

class BaseAuthSerializer(serializers.Serializer):
    """ The base of all Auth serializers
        that contains for email 
        authentications
    """
    email = serializers.CharField()

    def validate_email(self, email):
        """ Custom validator for email
            Raise ValidationError when email
            is not correct
        """
        if validate_email(email):
            raise serializers.ValidationError(_("Email is not valid!"))
        return email

class LoginSerializer(BaseAuthSerializer):
    """ Serializer for login API """
    password = serializers.CharField()

class RegisterSerializer(BaseAuthSerializer):
    """ Serializer for Register API """
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def validate_password(self, password):
        """ A function for validating password
            with default Django password validation
        """
        validate_password(password=password)
        return password

    def validate(self, validated_data):
        """ Custom validation error for passwords
            Raising validation error when passwords
            do not match or user already exists
        """
        if validator.check_user_existence(email=validated_data.get('email')):
            raise serializers.ValidationError(_('User is already exist'))
        validator.password_match_checker(
            validated_data.get('password'),
            validated_data.get('password_confirm')
        )
        return validated_data

class TokenSerializer(serializers.Serializer):
    """ Serializer for Response token
        to user at Login API
    """
    refresh = serializers.CharField()
    access = serializers.CharField()

class RefreshTokenSerializer(serializers.Serializer):
    """ Refresh token serializer for
        getting refresh token from frontend
        and set it on blacklist on LogoutAPIView
    """
    refresh = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    """ User serializer for response
        or any operation to user
    """
    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "is_active",
        ]
