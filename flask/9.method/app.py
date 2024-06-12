from flask import Flask,render_template,request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'pw': 'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw': 'hello'}
]

@app.route('/', methods=['GET','POST'])
def main():
    #id = request.args.get('id') GET 방식의 URL 파라미터를 처리할 때만 가능
    if request.method == 'POST':
        id = request.form['id'] # POST 방식 중에서 form-data를 처리할 때 payload를 받아오는 방식
        pw = request.form['password']

    #위에 있는 user목록과 입력한 id/pw를 비교해서 print로 로그인 허용 불허 출력
        user = next((user for user in users if user['id'] == id and user['pw'] == pw),None)
        if user:
            error = None
        else:
            error = "ID or PW 오류"

        #위 내용을 아래 html에 전달하시오
        return render_template('index.html',user=user,error=error) #post요청

    return render_template('index.html') #get요청

if __name__ == "__main__":
    app.run(debug=True)