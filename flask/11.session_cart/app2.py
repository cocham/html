from flask import Flask, session, render_template, redirect, url_for, request
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'cartttt123'
app.permanent_session_lifetime = timedelta(minutes=5) #5분후에 만료시키고자 함.

#사용자 DB
users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'pw': 'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw': 'hello'}
]

#상품 DB
items = {'item1':{'name':'상품1','price':1000,'image':'item1.jpg'},
        'item2':{'name':'상품2','price':2000,'image':'item2.jpg'},
        'item3':{'name':'상품3','price':3000,'image':'item3.jpg'}
        }

@app.route('/')
def main():
    return render_template('index2.html',items=items)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST': 
        #로그인 처리
        id = request.form['id'] 
        pw = request.form['pw']

        #이 사용자가 목록에 있는지 검사
        user = next((user for user in users if user['id'] == id and user['pw'] == pw),None)

        if user:
            session['user'] = user #로그인한 사용자 정보를 세션에 저장
            return redirect(url_for('cart'))
        else:
            return render_template('login.html',error="사용자 없음")
    
    return render_template('login.html') #get 요청

@app.route('/user/cart')
def cart():
    user = session.get('user') #위에서 내가 저장한 것 다시 불러오기
    print(session)
    if 'cart' not in session.get('user', {}):
        session['user']['cart'] = {}
    item_name = request.args.get('item_name')
    #카트에 물건 담기
    if item_name in session['user']['cart']:
        session['user']['cart'][item_name] += 1
    else:
        item_info = items.get(item_name)
        if item_info:
            session['user']['cart'][item_name] = 1
    session.modified = True
    print(session)

    return render_template('user_index.html',user=user,items=items)

@app.route('/view-cart')
def view_cart():
    cart_items = {}
    total_price = 0
    user = session.get('user')
    cart_items = user['cart']
    # 카트에 담긴 상품의 수량과 가격 조회
    for item_name,quantity in cart_items.items(): #세션 안의 cart라는 변수의 dict 객체들 가져오기
        item = items.get(item_name) #첫번째 항목의 아이템을 DB에서 조회하기
        if item:
            #프론트에서 표현하기 위한 key, value들 모아서 담기
            cart_items[item_name] = {'name': item['name'],'quantity':quantity, 'price':item['price'],'image':item['image']}
            total_price += item['price'] * quantity
    print(session)
    return render_template('cart2.html',user=user,cart_items=cart_items,total_price=total_price)


@app.route('/remove-item-from-cart/<item_name>')
def remove_item_from_cart(item_name):
    user = session.get('user')
    #상품 지우는 코드 작성
    if user['cart'] and item_name in user['cart']:
        user['cart'].pop(item_name)
        session.modified = True

    return redirect(url_for('view_cart'))

@app.route('/clear-cart')
def clear_cart():
    user = session.get('user')
    #카트 통째로 비우기 - 세션 내의 'cart'삭제하면 됨
    if user['cart']:
        user['cart'] = {}
        session.modified = True
        
    return redirect(url_for('view_cart'))

@app.route('/logout')
def logout():
    session.pop('user',None) #세션에서 사용자 user 정보 삭제(스택에 쌓여있는 내용을 지움)
    return redirect(url_for('main')) #로그아웃 이후 홈 페이지로 보내주기



if __name__ == "__main__":
    app.run(debug=True)