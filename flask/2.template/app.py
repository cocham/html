from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html"),200 #200이 기본형

@app.route('/user')
@app.route('/user/<name>')
def user(name=''):
    friends = ['bill','steve','larry']
    return render_template("user.html",username=name,content=friends) #서버사이드 렌더링

@app.route('/admin')
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(port=5000,debug=True)