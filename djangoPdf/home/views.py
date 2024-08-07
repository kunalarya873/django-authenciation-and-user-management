from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import StudentSerializer
from .helpers import save_pdf
import datetime
import pandas as pd
from django.conf import settings
import uuid
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

class GeneratePdf(APIView):
    def get(self, request):
        student_objs = Student.objects.all()
        params = {
            'today': datetime.date.today(),
            'student_objs': student_objs
        }
        try:
            file_name, success = save_pdf(params)
            if not success:
                return Response({'status': 'Failed to generate PDF'}, status=status.HTTP_400_BAD_REQUEST)
            
            file_path = f'/public/static/{file_name}'
            return Response({"status": 'PDF generated successfully', 'path': file_path}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': f'Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ExportImportExcel(APIView):

    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        df = pd.DataFrame(serializer.data)
        print(df)
        df.to_csv(f"public/static/excel/{uuid.uuid4()}.csv", encoding="UTF-8")
        return Response({'status': 200})
    
    def post(self, request):
        excel_upload_obj = ExcelFileUpload.objects.create(excel_file_upload = request.FILES['files'])
        df = pd.read_csv(f'public/static/{excel_upload_obj.excel_file_upload}')
        print(df.values.tolist())
        return Response({'status': 200})
