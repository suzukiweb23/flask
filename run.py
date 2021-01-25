from flask import Flask
from flask_mail import Mail, Message
from func import test
import config

def create_app():
    app = Flask(__name__)
    return app
    
app = create_app()

# 分割したblueprintを登録する
app.register_blueprint(test.app)
app.config.from_object('config')

#これがないとBlueprintに登録したAPIにランタイムエラーが出る。
mail = Mail(app)

@app.route('/')
def hello():
#    msg = Message('Hello', sender = 'XXXXXXX@gmail.com', recipients = ['XXXXXXX@gmail.com'])
#    msg.body = "Hello Flask message sent from Flask-Mail"
#    mail.send(msg)
    name = "Hello World"
    return name

if __name__ == '__main__':
    app.run(debug=True)
