from app import mail
from flask_mail import Message

# def send_mail(to, subject, template):
def send_mail():
    msg = Message('测试邮件',
                  sender='453431821@qq.com', body='Test', recipients=['453431821@qq.com'])
    mail.send(msg)
