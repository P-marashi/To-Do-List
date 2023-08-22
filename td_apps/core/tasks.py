from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from config.tools.celery import app


# Email content template for OTP
OTP_CONTENT = """{name} عزیز!
به وبسایت {website_name} خوش آمدید!

کد ورود شما به وبسایت: {otp_code}
"""
@app.task
def send_otp_email(to_email, otp_code):
    """ A Celery shared task for sending OTP code to the given email address """
    send_mail(
        subject=f"کد ورود به {settings.SITE_NAME}",
        message= OTP_CONTENT,  # We use the html_message parameter to send HTML content
        from_email= None,
        recipient_list=[to_email]
    )
    return 1