from django.core.cache import cache

def cache_otp(name, code):
    """ Helper function for caching OTP """
    cached_data = cache.set(name, code, timeout=120000)  # Cache the OTP with a timeout of 120000 seconds
    return cached_data

def get_cached_otp(name):
    """ Helper function for getting cached OTP """
    cached_otp = cache.get(name)  # Retrieve the cached OTP by its name
    return cached_otp
