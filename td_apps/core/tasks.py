from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

# Email content template for OTP
OTP_CONTENT = """{name} عزیز!
به وبسایت {website_name} خوش آمدید!

کد ورود شما به وبسایت: {otp_code}
"""

@shared_task
def send_otp_email(to_email, otp_code):
    """ A Celery shared task for sending OTP code to the given email address """
    send_mail(
        subject=f"کد ورود به {settings.SITE_NAME}",
        message="",  # We use the html_message parameter to send HTML content
        html_message=OTP_CONTENT.format(
            name=to_email,
            website_name=settings.SITE_NAME,
            otp_code=otp_code
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to_email]
    )
    return 1
