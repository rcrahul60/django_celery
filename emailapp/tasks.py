from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


@shared_task(bind=True)
def sendMaill(self):
    users = get_user_model().objects.all()
    for user in users:
        message = 'you got the message'
        mail_subject = "hi celery docs"
        to_mail = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email='rcrahul60@gmail.com',
            recipient_list=[to_mail],
            fail_silently=True
        )
    return 'done'