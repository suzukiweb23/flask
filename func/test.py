from flask import Flask, Blueprint, current_app
from flask_mail import Mail, Message

#これがないとインスタンスが作成されない。
mail = Mail()
# Blueprintのオブジェクトを生成する
app = Blueprint('func', __name__)

@app.route('/test')
def func_2():
    msg = Message('Hello', sender = 'XXXXXXXX@gmail.com', recipients = ['XXXXXXXX@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return 'Test'
