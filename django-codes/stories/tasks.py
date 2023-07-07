import time
from celery import shared_task
from core.models import Subscribers
from stories.models import Recipe
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@shared_task
def export_data():
    print('Process Start')
    time.sleep(10)
    print('Process End')


@shared_task
def send_email_to_subs():
    email_lists = Subscribers.objects.values_list('email', flat=True)
    recipes = Recipe.objects.all()
    message = render_to_string('email-subscribers.html', {
                'recipes' : recipes

            })
    subject = 'New Blog Posts'
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_lists)
    mail.content_subtype = 'html'
    mail.send()


