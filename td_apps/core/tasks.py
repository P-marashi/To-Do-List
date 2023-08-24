from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from config.tools.celery import app


# Email content template for OTP
OTP_CONTENT = """
<p>{username} عزیز!</p>
<p>وبسایت {website_name} خوش آمدید به</p>
<p>کد ورود شما به وبسایت: <strong>{otp_code}</strong></p>
"""
@shared_task
def send_otp_email(to_email, otp_code):
    """ A Celery shared task for sending OTP code to the given email address """
    formatted_content = OTP_CONTENT.format(
        username=to_email,
        website_name=settings.SITE_NAME,
        otp_code=otp_code
    )
   
    send_mail(
        subject=f"کد ورود به {settings.SITE_NAME}",
        message="",  # Leave this empty since you're using `html_message`
        html_message=formatted_content,  # Use the formatted content here
        from_email=None,
        recipient_list=[to_email]
    )
    
    return 1