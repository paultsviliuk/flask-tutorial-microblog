from flask_mail import Message
from app import mail


def send_mail(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text.body
    msg.html = html.body
    mail.send(msg)

