from celery import Celery
from celery.schedules import crontab

# init celery
celery = Celery(
    'tasks',
    broker = 'redis://localhost:6379/0'
)

# config the time
celery.conf.update(
    timezone = 'Asia/Kolkata',
    enable_utc = False,
)

import csv
import time

@celery.task()
def generate_csv(data, filename='report.csv'):

    time.sleep(30)
    
    with open(filename, mode='w', newline='') as f:
        
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

from app import app
from models import User
from mail import send_mail

@celery.task()
def daily_reminders():
    with app.app_context():
        for user in User.query.all():
            send_mail(user.email, 'Hey user!', 'Forgot to visit the application?')

from datetime import timedelta

# scheduled tasks
celery.conf.beat_schedule = {
    'daily_reminders_mails': {
        'task': 'celery_app.daily_reminders',
        # 'schedule': crontab(hour=18, minute=30)
        'schedule': timedelta(seconds=10)
    }
}