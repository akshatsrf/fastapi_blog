from celery import Celery
import smtplib
from base64 import b64decode

app = Celery('tasks',
             broker='amqp://uwvixavr:MtPVnhDmZKcIWbfyAGDzCU8SBieiSAWD@turkey.rmq.cloudamqp.com/uwvixavr',
             backend='db+sqlite:///db.celery_data')

app.send_task()
@app.task
def send_mail():
    sender = '2018pietcsakshat12@poornima.org'
    receivers = ['2018pcecsvishwas179@poornima.org']
    message = "Hello"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("2018pietcsakshat12@poornima.org",b64decode("YWtzaGF0QDEyMw==").decode("ascii"))
    s.sendmail(sender, receivers, message)   
    s.quit()       
    print("Done")