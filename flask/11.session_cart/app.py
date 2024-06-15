from flask import Flask, session, render_template, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'cartttt123'
app.permanent_session_lifetime = timedelta(minutes=5) #5분후에 만료시키고자 함.

#상품 DB
items = {'item1':{'name':'상품1','price':1000,'image':'item1.jpg'},
        'item2':{'name':'상품2','price':2000,'image':'item2.jpg'},
        'item3':{'name':'상품3','price':3000,'image':'item3.jpg'}
        }

@app.route('/')
def main():
    return render_template('index.html',items=items)

@app.route('/add-to-cart/<item_name>') #원래 변수 작명 시에는 동사 안 넣는 게 좋음. 왜냐 메소드에 담겨있으므로
def add_to_cart(item_name):
    print(f"상품담기: {item_name}")
    #상품을 세션안의 cart라는 변수에 담기
    if 'cart' not in session:
        session['cart'] = {}

    #카트에 물건 담기
    if item_name in session['cart']: #이전에 담은 적이 있는 상품인가?
        session['cart'][item_name] += 1 #있으면 개수를 1증가
    else: #이전에 담은적이 없으면
        item_info = items.get(item_name) #해당 상품을 상품DB에서 조회하기
        if item_info:
            session['cart'][item_name] = 1

    #세션 정보가 변경된 것을 알려주기
    session.modified = True
    print(session)
    return redirect(url_for('main'))

@app.route('/remove-item-from-cart/<item_name>')
def remove_item_from_cart(item_name):
    print(f"상품 지우기 {item_name}")

    #상품 지우는 코드 작성
    if 'cart' in session and item_name in session['cart']:
        session['cart'].pop(item_name)
        session.modified = True

    return redirect(url_for('view_cart'))

@app.route('/clear-cart')
def clear_cart():
    #카트 통째로 비우기 - 세션 내의 'cart'삭제하면 됨
    if 'cart' in session:
        session.pop('cart')
        session.modified = True
        
    return redirect(url_for('view_cart'))

@app.route('/view-cart')
def view_cart():
    cart_items = {}
    total_price = 0

    #카트에 담긴 상품의 수량과 가격 조회
    for item_name,quantity in session.get('cart', {}).items(): #세션 안의 cart라는 변수의 dict 객체들 가져오기
        item = items.get(item_name) #첫번째 항목의 아이템을 DB에서 조회하기
        if item:
            #프론트에서 표현하기 위한 key, value들 모아서 담기
            cart_items[item_name] = {'name': item['name'],'quantity':quantity, 'price':item['price'],'image':item['image']}
            total_price += item['price'] * quantity

    return render_template('cart.html',cart_items=cart_items,total_price=total_price)


if __name__ == "__main__":
    app.run(debug=True)