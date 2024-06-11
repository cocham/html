from flask import Flask,render_template,request
import csv

app = Flask(__name__)

csv_data = []
headers = []

def load_csv_data(filename):
    global headers #전역 변수 변경 선언

    with open(filename,newline='',encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        headers = [fieldname.strip() for fieldname in csv_reader.fieldnames] #fieldnames는 csv 파일의 각 열 이름을 가져옴
        for row in csv_reader:
            clean_row = {fieldname.strip():value.strip() for fieldname,value in row.items()} #양쪽 공백 제거해서 키값으로 넣어줌
            csv_data.append(clean_row)

def paginate_data(page_number, per_page,data_list):
    start_index = (page_number - 1) * per_page
    end_index = start_index + per_page
    return data_list[start_index:end_index]

@app.route('/')
@app.route('/<int:page>')
def index(page=1):
    # 페이지당 항목 수 설정
    per_page = 10
    
    # 전체 페이지 수 계산
    total_pages = len(csv_data) // per_page + (1 if len(csv_data) % per_page > 0 else 0)
    
    # 현재 페이지에 해당하는 데이터 추출
    current_data = paginate_data(page,per_page,csv_data)
    
    # 템플릿 렌더링(index2.html안의 변수에 flask 변수 전달)
    return render_template('index2.html', headers=headers, users=current_data, total_pages=total_pages)

@app.route('/user')
def get_user_by_name():
    search_name = request.args.get('name')
    get_user = [x for x in csv_data if x['Name'] == search_name]

    per_page = 5
    total_pages = len(get_user) // per_page + (1 if len(get_user) % per_page > 0 else 0)
    page = request.args.get('page',default=1,type=int)
    current_data = paginate_data(page,per_page,get_user)
    return render_template('index2.html',headers=headers,users=get_user,total_pages=total_pages)

if __name__ == "__main__":
    load_csv_data('./data.csv')
    #print(csv_data)
    app.run(debug=True)