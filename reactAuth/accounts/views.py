from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
import logging
from .helpers import *
logger = logging.getLogger(__name__)

class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)

            if not serializer.is_valid():
                return Response({
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({'message': 'An email OTP sent on your number and email'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Registration failed: {e}")
            return Response({'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class verifyOtp(APIView):
    def post(self, request):
        try:
            data = request.data
            user_obj = User.objects.get(phone = data.get('phone'))
            otp = data.get('otp')
            if user_obj.otp == otp:
                user_obj.is_phone_verified = True
                user_obj.save()
                return Response({"status": 200, "message": "Your OTP is verified"})
            return Response({'status': 403, 'message': 'otp is wrong'})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "something went wrong"})
        
    def patch(self, request):
        try:
            if not User.objects.filter(phone = data.get('phone')).exists():
                return Response({'status': 200, 'message': 'User already exists'})
            data = request.data
            if send_otp_to_mobile(data.get('phone')):
                return Response({'status': 200, 'message': 'new otp send'})
            return Response({'status': 200, 'message': 'new otp send'})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "something went wrong"})
