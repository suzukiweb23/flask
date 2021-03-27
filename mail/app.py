from flask import Flask, request, Markup, abort, render_template, Blueprint
from flask_mail import Mail, Message
from rest import api, auth
import config

def create_app():
    app = Flask(__name__)
    return app
    
app = create_app()

db = SQLAlchemy(app)

# 分割したblueprintを登録する
app.register_blueprint(api.app)
app.register_blueprint(auth.app)
app.config.from_object('config')

#これがないとBlueprintに登録したAPIにランタイムエラーが出る。
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

#def index():
#    return 'Logout'

if __name__ == '__main__':
    app.run(debug=True)
