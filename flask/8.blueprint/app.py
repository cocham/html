from flask import Flask,render_template
from admin.admin import admin_app
from product.product import product_app
from user.user import user_app

app = Flask(__name__)

app.register_blueprint(admin_app,url_prefix='/admin')
app.register_blueprint(product_app,url_prefix='/product')
app.register_blueprint(user_app,url_prefix='/user')


@app.route('/') #여기서의 /는 blueprint를 등록한 app에서 정의한 prefix가 기본값
def main():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)