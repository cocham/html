from flask import Flask

app = Flask(__name__) #__name__은 파일명을 플라스크로 칭함

@app.route("/") #데코레이터로 라우팅 정의
def home():
    return "<html><body><h1>Hello, Welcome to 내 플라스크 서버</h1><p>여기는 나의 문장이 들어갑니다.</p></body></html>"

@app.route("/user/")
@app.route("/user/<name>") #<name>변수임 -> 이 변수명과 함수의 인자를 매칭해서 내부에서 처리
def user(name=None):
    username = name

    return f'''<html><body><h1>사용자 페이지: {username} 님 안녕하세요.
                </h1><p>여기는 나의 문장이 들어갑니다.</p>
                </body></html>'''

@app.route("/admin")
def admin():
    return "<html><body><h1>관리자 페이지</h1><p>여기는 나의 문장이 들어갑니다.</p></body></html>"


if __name__ == "__main__":
    app.run(port=5000, debug=True) #개발 환경에서만 debug사용 *production에서는 debug는 항상 OFF..
    