from flask import Flask, render_template, request
import database as db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

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
    if (request.method == 'POST'):
        email = request.form['email']
        password = request.form['password']
        db.add_user(email, password)
        print(email, password)
        return "Hello"
    return render_template('register.html')

if __name__ == '__main__':
    app.run()
