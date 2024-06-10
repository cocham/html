from flask import Flask,jsonify

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-123'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-234'},
    {'name': 'Charlie', 'age': 35, 'phone': '555-555-555'}
]


@app.route('/')
def home():
    return jsonify(users)

@app.route('/user/<name>')
def search_user(name):
    user = None
    for u in users:
        if u['name'].lower() == name.lower():
            user = u
            break
    #결과가 있을 때는 지금 처럼 응답과 200을 보내지만 없을 때는? 응답값에 404 출력
    if user:
        return jsonify(user),200
    else:
        return jsonify({'ERROR': 'USER NOT FOUND'}),404

if __name__ == "__main__":
    app.run(debug=True)