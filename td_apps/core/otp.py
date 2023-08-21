import random

def otp_generator():
    """ Generate a random 5-digit OTP code """
    return random.randrange(10000, 99999)
