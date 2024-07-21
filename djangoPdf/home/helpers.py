from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import uuid
import os
from django.conf import settings

def save_pdf(params: dict):
    template = get_template("pdf.html")
    html = template.render(params)
    file_name = f'{str(uuid.uuid4())}.pdf'
    file_path = os.path.join(settings.BASE_DIR, 'public', 'static', file_name)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, 'wb+') as output:
            pdf = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), dest=output)
            return (None, False) if pdf.err else (file_name, True)
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return str(e), False
