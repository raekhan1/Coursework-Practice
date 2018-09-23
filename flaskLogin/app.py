from flask import Flask, render_template, request, flash,redirect,url_for
import database as db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/rae')
def rae():
    return render_template('hello.html', name="Sam")


@app.route('/name')
def name():
    nameq = request.args.get('rae')
    return render_template('hello.html', name=nameq)


@app.route('/<name>')
def namedurl(name):
    return render_template('hello.html', name=name)


@app.route('/register', methods={'GET', 'POST'})
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        re_password = request.form['re_password']

        if db.add_user(email, password,re_password):
            print(email, password)
            return "You are now registered"
        else:
            return "Your passwords don't match"
    return render_template('register.html')


@app.route('/login',methods={'GET','POST'})
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if db.check_user(email, password):
            print('logged in')
            return render_template('hello.html', name=email)
        else:
            return "password or username is incorrect"

    return render_template('login.html')


@app.route('/forgetpass', methods={'GET', 'POST'})

def forget_pass():
    if request.method == 'POST':
        email = request.form['email']
        if db.fp_check_user(email):

            return 'you are a user'
        else:
            return "You are not a user "

    return render_template('forgetpass.html')


if __name__ == '__main__':
    app.run()
