from django.shortcuts import render
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import HttpResponse
import mailTrap as mt
import base64
from decouple import config
# Create your views here.
def home(request):
    return render(request, "myapp/home.html")


def send_test_email(request):
    subject = "SUBJECT"
    name = 'Kunal'
    email = 'aqa@af.cc'
    plain_message = "hello"
    from_email = ''
    to_email = ''

    html_message = render_to_string('myapp/email_template.html', {'name'
    : name, 'email': email})
    html_message = strip_tags(html_message)

    #Create email with plain text message
    email_w_text =EmailMessage(subject=subject,
                 body=plain_message,
                 from_email='admin@example.com',
                 to=["dcdsc@dcvs.cc"])
    
    #Create email with html message
    email_w_html = EmailMessage(subject=subject,
                 body=html_message,
                 from_email='admin@example.com',
                 to=["dcdsc@dcvs.cc"])
    
    # set email type html/text Content
    email_w_text_and_html = EmailMultiAlternatives(subject=subject,
                 body=plain_message,
                 from_email='admin@example.com',
                 to=["dcdsc@dcvs.cc"])
    email_w_text_and_html.attach_alternative(html_message, "text/html")

    # set email type html/text with attachment
    email_w_attachment = EmailMultiAlternatives(subject=subject,
                 body=html_message,
                 from_email='admin@example.com',
                 to=["dcdsc@dcvs.cc"])
    with open('SQL_Resume.pdf', 'rb') as file:
        email_w_attachment.attach('SQL_Resume.pdf', file.read(), 'application/pdf')
    email_w_attachment.attach_alternative(html_message, "text/html")
    #send email
    email_w_attachment.send()
    return HttpResponse("Email Sent")


def send_prod_smtp_email(request):
    subject = "SMTP TESTING USING MAILTRAP"
    name = 'Kunal'
    email = 'email.example@kunal.com'
    html_message = render_to_string('myapp/email_template.html', {'name'
    : name, 'email': email})
    html_message = strip_tags(html_message)
    from_email = 'kunal@demomailtrap.com'
    to_email = ['kunalarya873@gmail.com']

    email_smtp = EmailMultiAlternatives(subject=subject,
                 body=html_message,
                 from_email=from_email,
                 to=[to_email])
    email_smtp.attach_alternative(html_message, "text/html")

    email_smtp.send()

    return HttpResponse("SMTP email is send to your emailID")



def send_prod_api_email(req):  # For Production using API
    subject = 'Test API Email'
    name = 'User'
    email = 'sss@email.com'
    html_message = render_to_string(
        'myapp/email_template.html', {'name': name, 'email': email})
    plain_message = strip_tags(html_message)
    from_email = 'admin@demomailtrap.com'
    to_email = 'msjdmf@sdcsd.com'

    # Attach File to EMail
    with open('SQL_Resume.pdf', 'rb') as file:
        file_content = base64.b64encode(file.read())

    myfile = mt.Attachment(
        content=file_content,
        filename="myfile.pdf",
        mimetype="application/pdf"
    )

    mail = mt.Mail(
        sender=mt.Address(email=from_email, name="Admin"),
        to=[mt.Address(email=to_email, name=name)],
        subject=subject,
        text=plain_message,
        html=html_message,
        category="OTP Emails",
        attachments=[myfile]
    )

    client = mt.MailClient(token=config('API_KEY'))
    client.send(mail)

    return HttpResponse('API Email with HTML and attachment sent successfully.')