from django.shortcuts import render
from django.core.mail import send_mail
from celery import shared_task
from .tasks import convert_doc_to_pdf
from django.http import HttpResponseRedirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from celery.result import AsyncResult
import os

# Create your views here.

def index(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage(location='uploads/')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        task = convert_doc_to_pdf.delay(filename)
        return HttpResponseRedirect(f'/status/{task.id}/')
        
    return render(request, 'index.html')

def check_status(request, task_id):
    res = AsyncResult(task_id)
    if res.ready():
        pdf_file_path = res.result
        context = {
            'task_status': res.ready(),
            'pdf_file_url': pdf_file_path
        }
    else:
        context = {'task_status': res.ready()}
    return render(request, 'progress.html', context)

def download_file(request, file_path):
    file_path = os.path.join('uploads/', file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = f'inline; filename={os.path.basename(file_path)}'
            return response
    return HttpResponse('File not found')
@shared_task
def send_mail_with_celery():
    send_mail("CELERY WORKED", "CELERY BODY", "justkunal@gmail.com",
              ["kunalarya873@gmail.com"], fail_silently=False)
    return None
