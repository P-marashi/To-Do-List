from django.contrib.auth import get_user_model
# import DRF here
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
# import spectacular 
from drf_spectacular.utils import extend_schema, OpenApiParameter
# Local app 
from .serializers import RegisterSerializer, LoginSerializer, TokenSerializer, VerifyURLSerializer
from .backend import email_authentication
from td_apps.core.otp import otp_generator
from td_apps.core.cache import cache_otp
from td_apps.core.tasks import send_otp_email
from td_apps.core.tokens import one_time_token_generator


# declared needed api parameters on @extend_schema it will be use 
ONE_TIME_LINK_API_PARAMETERS = [
    OpenApiParameter(
        'uidb64',
        type=str,
        location=OpenApiParameter.PATH,
        description="User primary key encoded in base64",
    ),
    OpenApiParameter(
        'token',
        type=str,
        location=OpenApiParameter.PATH,
        description="One-time generated token",
    )
]

class AuthViewSet(viewsets.ViewSet):
    """
    ViewSet for user authentication.
    """

    @action(detail=False, methods=['post'])
    def login(self, request):
        """ Log in a user """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        # Authenticate user using custom email authentication backend
        user = email_authentication.authenticate(email=email, password=password) 
        if user and user.is_active:
            # Generate tokens and return them in response
            tokens = email_authentication.generate_token(user)
            return Response(data=TokenSerializer(tokens).data, status=status.HTTP_200_OK)
        return Response(data={'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def register(self, request):
        """ Register the user """
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        
        # Generate OTP and cache it
        otp = otp_generator()
        print(otp)
        cache_otp(email, otp)

        # Create a new user
        user = get_user_model().objects.create_user(
            email=email, password=password)

        send_otp_email.delay(email, otp)
        # Generate and return a verification URL
        url = one_time_token_generator.create_url_activation(user)
        return Response(data=VerifyURLSerializer({'url': url}).data, status=status.HTTP_201_CREATED)
