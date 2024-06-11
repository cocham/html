from flask import Flask,render_template,request
import csv

app = Flask(__name__)

csv_data = []
headers = []
def load_csv_data(filename):
    global headers
    with open(filename,newline='',encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader) #헤더 추출
        for row in csv_reader:
            csv_data.append(row)

'''
@app.route('/')
def index():
    return render_template('index.html', users=csv_data)
'''
def paginate_data(page_number, per_page,data_list):
    start_index = (page_number - 1) * per_page
    end_index = start_index + per_page
    return data_list[start_index:end_index]

@app.route('/')
@app.route('/<int:page>')
def index(page=1):
    # 페이지 번호와 페이지당 항목 수 설정
    per_page = 20
    
    # 전체 페이지 수 계산
    total_pages = len(csv_data) // per_page + (1 if len(csv_data) % per_page > 0 else 0)
    
    # 현재 페이지에 해당하는 데이터 추출
    current_data = paginate_data(page, per_page, csv_data)
    
    # 템플릿 렌더링
    return render_template('index.html', headers=headers, users=current_data, total_pages=total_pages)

@app.route('/user')
def get_user_by_name():
    search_name = request.args.get('name')
    get_user = [x for x in csv_data if x[1] == search_name]
    
    per_page = 5 #페이지 당 보여줄 항목 개수
    total_pages = len(get_user) // per_page + (1 if len(get_user) % per_page >0 else 0)
    page = request.args.get('page',default=1,type=int) #page_num을 받아와서 검색 페이지 동적으로 생성
    current_data = paginate_data(page,per_page,get_user)
    
    print(total_pages)
    return render_template("index.html",headers=headers,users=current_data,total_pages=total_pages)


if __name__ == "__main__":
    load_csv_data('./user.csv')
    #print(csv_data)
    app.run(debug=True)