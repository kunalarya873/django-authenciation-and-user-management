import random
from django.core.cache import cache

def send_otp_to_mobile(mobile, user_obj):
    if cache.get(mobile):
        return False
    try:
        otp_to_send = random.randint(1000, 9999)
        cache.set(mobile, otp_to_send, timeout=60)
        user_obj.otp = otp_to_send
        user_obj.save()
        return True
    except Exception as e:
        print(e)
