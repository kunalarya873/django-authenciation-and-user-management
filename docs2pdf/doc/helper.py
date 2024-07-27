from django.core.mail import send_mail
def send_mail_task_without_celery():
    send_mail('Hello', 'Hello', 'withoutcelery.com', ['kunalarya873@gmail.com'], fail_silently=False)
    return None