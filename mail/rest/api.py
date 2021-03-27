from flask import Flask, Blueprint, current_app, request, Markup, abort, render_template
from flask_mail import Mail, Message

#これがないとインスタンスが作成されない。
mail = Mail()
# Blueprintのオブジェクトを生成する
app = Blueprint('api', __name__)

@app.route('/apiname',methods=['GET', 'POST'])
def func_1():
    msg = Message('Hello', sender = 'unicia127@gmail.com', recipients = ['suzukiweb23@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    try:
        if request.method == 'GET':
            return request.args.get('request_args', '')
        elif request.method == 'POST':
            return request.form['request_args']
        else:
            return abort(400)
    except Exception as e:
        return str(e)

@app.route('/apiname2',methods=['GET', 'POST'])
def func_2():
    return render_template('send_get.html')

# getでの入力情報処理
@app.route("/receive_get", methods=["GET"])
def receive_get():
    name = request.args["my_name"]
    if len(name) == 0:
        return "名前が未入力です"
    else:
        return 'あなたが入力した名前は' + str(name) + "です"

# post処理の入力フォームを表示
@app.route("/request_post", methods=["GET"])
def post_sample():
    return render_template('send_post.html')

# postでの入力情報処理
@app.route("/request_post", methods=["POST"])
def post_action():
    if "gender" in request.form.keys():
        gender = request.form["gender"]
        if gender == "男":
            sex = '男性'
        elif gender == "女":
            sex = "女性"
    else:
        sex = '性別不明'
    if 'age' in request.form.keys():
        age_range = request.form['age']
    else:
        age_range = '年齢不詳'
    return f'あなたは{sex}で{age_range}です。'