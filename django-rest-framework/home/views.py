from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



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
        token_obj, _ = Token.objects.get_or_create(user=user)

        return Response({'status': 200,'payload': serializer.data,'token':str(token_obj), 'message': 'you sent'})


class StudentAPI(APIView):
    authentication_classes = [ TokenAuthentication]
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

    
'''@api_view(['GET'])  # specify the allowed HTTP methods
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data= request.data)
    if not serializer.is_valid():
        return Response({'status': '403', 'message': serializer.errors})
    serializer.save()
    return Response({'status': 200, 'payload': serializer.data, 'message': 'you sent'})


@csrf_exempt
@api_view(['PUT'])
def update_student(request, id):
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

@csrf_exempt
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status': 200, 'message': 'deleted'})
    except Student.DoesNotExist:
        return Response({'status': 404, 'message': 'invalid id'})
    except Exception as e:
        return Response({'status': 500, 'message': str(e)})'''