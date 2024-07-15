from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics


#Here we don't create any method
class StudentGeneric(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentGeneric1(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'






@api_view(['GET'])  # specify the allowed HTTP methods
def get_book(request):
    book_objs = Books.objects.all()
    serializers = BookSerializer(book_objs, many=True)
    return Response({'status': '200', 'payload': serializers.data})

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':'403', 'message': serializer.errors, 'message': 'your data is sent'})
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({'status': 200,'payload': serializer.data,'refresh':str(refresh),'access': str(refresh.access_token), 'message': 'you sent'})


class StudentAPI(APIView):
    authentication_classes = [ JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        return Response({'status': '200', 'payload': serializer.data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': '403', 'message': serializer.errors})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'you sent'})

    def put(self, request, id=None):
        try:
            student_obj = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'status': '404', 'message': 'invalid id'})
        serializer = StudentSerializer(student_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is sent'})
        else:
            # Log the request data and serializer errors for debugging
            print("Request data:", request.data)
            print("Serializer errors:", serializer.errors)
            return Response({'status': '403', 'errors': serializer.errors, 'message': "update failed"})

    def delete(self, request, id=None):
        try:
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({'status': 200, 'message': 'deleted'})
        except Student.DoesNotExist:
            return Response({'status': 404, 'message': 'invalid id'})
        except Exception as e:
            return Response({'status': 500, 'message': str(e)})

    def patch(self, request):
        try:
            student_obj = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': '403', 'message': serializer.errors})
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is sent'})
        except Exception as e:
            return Response({'status': 500, 'message': e})
        
    def update(self, request):
        try:
            student_obj = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data, partial=False)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': '403', 'message': serializer.errors})
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is sent'})
        except Exception as e:
            return Response({'status': 500, 'message': e})
