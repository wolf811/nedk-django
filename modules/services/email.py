from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# from django.contrib.auth.models import User


def send_contact_email_message(subject, phone, email, service, content, ip, name):
    """
    Function to send contact form email
    """
    # user = User.objects.get(id=user_id) if user_id else None
    message = render_to_string('mainapp/email/feedback_email_send.html', {
        'subject': subject,
        'phone': phone,
        'email': email,
        'service': service,
        'content': content,
        'ip': ip,
        'name': name,
    })
    email = EmailMessage(message, settings.SERVER_EMAIL, settings.EMAIL_ADMIN)
    email.send(fail_silently=False)
