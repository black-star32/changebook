from flask import current_app, render_template

from app import mail
from flask_mail import Message

def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件',
    #               sender='453431821@qq.com', body='Test', recipients=['453431821@qq.com'])
    msg = Message('[ChangeBook]' + '' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
