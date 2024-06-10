from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-1238'},
    {'name': 'Alice', 'age': 30, 'phone': '123-321-4321'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-2347'},
    {'name': 'Charlie', 'age': 35, 'phone': '555-555-5554'}
]

@app.route('/')
def home():
    return jsonify(users)

@app.route('/search')
def search():
    name_query = request.args.get('name')
    age_query = request.args.get('age')
    phone_query = request.args.get('phone')
    result = []
    
    '''
    page = request.args.get('page',default=1,type=int)
    print(query,page)
    return f"검색중: {query} on 페이지 {page}...",200
    '''

    #name쿼리가 주어지고 나이나 폰끝자리를 매칭시켜 user 찾기
    if name_query:
        result = [u for u in users if name_query.lower() == u['name'].lower() ]

    if age_query:
        try:
            age_query = int(age_query)
            result = [u for u in result if age_query == u['age']]
        except ValueError:
            return jsonify({"error": "Age parameter must be an integer"}), 400
    
    if phone_query:
        try:
            phone_query = int(phone_query)
            result = [u for u in result if phone_query == int(u['phone'][-4:])]
        except ValueError:
            return jsonify({"error": "Phone parameter must be an integer"}), 400

    if result:
        return jsonify(result)
    else:
        return jsonify({'error':'user not found'}), 404
    
    '''result = [u for u in users if u['name'].lower() == name_query.lower() and 
            str(u['age']) == age_query and 
            u['phone'][-4:] == phone_query]
    return jsonify(result)'''


if __name__ == "__main__":
    app.run(debug=True)