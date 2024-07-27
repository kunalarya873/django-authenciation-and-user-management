from celery import shared_task
from docx2pdf import convert
import os
import tempfile

@shared_task
def convert_doc_to_pdf(filename):
    input_path = os.path.join('uploads', filename)
    output_path = input_path.replace('.docx', '.pdf')
    convert(input_path, output_path)
    return output_path

@shared_task
def send_mail_with_celery():
    send_mail("CELERY WORKED", "CELERY BODY", "justkunal@gmail.com",
              ["kunalarya873@gmail.com"], fail_silently=False)
    return None
