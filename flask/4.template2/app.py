from flask import Flask, render_template,request

app = Flask(__name__)

#users = ['Alice','Bob','Charlie','David','Eve','Frank']
users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-1238'},
    {'name': 'Alice', 'age': 30, 'phone': '123-321-4321'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-2347'},
    {'name': 'Charlie', 'age': 35, 'phone': '555-555-5554'}
]

@app.route('/')
def main():
    return render_template("index.html",users=users) 

@app.route('/user')
def get_users_by_name_age():
    search_name = request.args.get('name')
    search_age = request.args.get('age')

    filtered_user = users

    if search_name:
        filtered_user = [u for u in filtered_user if search_name.lower() == u['name'].lower()]

    if search_age:
        filtered_user = [u for u in filtered_user if int(search_age) == u['age']]

    return render_template('index.html',users=filtered_user)

    
'''
특정 스펠링으로 시작하는 사람..?
나이가 특정 나이보다 많은 사람..?

'''

if __name__ == "__main__":
    app.run(debug=True)