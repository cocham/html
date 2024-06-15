from flask import Flask,render_template,request
import csv

app = Flask(__name__)

csv_data = []
headers = ['index']

def load_csv_data(filename):
    global headers #전역 변수 변경 선언

    with open(filename,newline='',encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        headers.extend([fieldname.strip() for fieldname in csv_reader.fieldnames]) #fieldnames는 csv 파일의 각 열 이름을 가져옴
        for row in csv_reader:
            clean_row = {fieldname.strip():value.strip() for fieldname,value in row.items()} #양쪽 공백 제거해서 키값으로 넣어줌
            csv_data.append(clean_row)

def paginate_data(page_number, per_page, data_list):
    start_index = (page_number - 1) * per_page
    end_index = start_index + per_page
    return data_list[start_index:end_index]

@app.route('/')
def index():
    page = request.args.get('page',default=1,type=int)
    search_name = request.args.get('name',default='',type=str) #아무것도 입력 안 한 상태에서 검색을 누르면 홈으로 되돌아 갈 수 있게..
    per_page = request.args.get('per_page',default=10,type=int)
    
    get_user = [x for x in csv_data if search_name in x['name']]
    start_index = (page-1) * per_page
    total_pages = len(get_user) // per_page + (1 if len(get_user) % per_page > 0 else 0)
    current_data = paginate_data(page,per_page,get_user)
    
    render_dict = {
    'headers':headers,
    'users':current_data,
    'total_pages':total_pages,
    'start_index':start_index,
    'page':page,
    'per_page':per_page,
    'search_name':search_name
    }

    return render_template('index5.html',**render_dict)


@app.route('/user/<uuid>')
def user_detail(uuid):
    #해당 UUID에 해당하는 사용자를 찾아서 데이터를 전달한다.
    user = [x for x in csv_data if x['id'] == uuid]
    return render_template('user_detail.html',user=user,headers=headers)


if __name__ == "__main__":
    load_csv_data('./data.csv')
    #print(csv_data)
    app.run(debug=True)