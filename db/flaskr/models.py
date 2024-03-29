# models.py
#from flaskr import db, login_manager
from flaskr import db
#from flask_bcrypt import generate_password_hash, check_password_hash
#from flask_login import UserMixin

# セッションに保存されたログインユーザを返すためにtemplateから呼ばれる
#@login_manager.user_loader
#def load_user(user_id):
#    return User.query.get(user_id)

# UserMixinはFLask-Loginライブラリを利用するユーザが持つべきオブジェクトを定義
#class User(UserMixin, db.Model):
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password, password)

    def add_user(self):
        with db.session.begin(subtransactions=True):
            db.session.add(self)
        db.session.commit()
    
    #@classmethod
    #def select_by_email(cls, email):
    #    return cls.query.filter_by(email=email).first()
