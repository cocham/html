from flask import Blueprint,render_template

admin_app = Blueprint('admin', __name__) #블루프린트 명칭 지정

@admin_app.route('/')
def main():
    return render_template('admin/index.html')
