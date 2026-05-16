from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        action = request.form.get('action')
        
        # 1. منطق الفيزياء
        if action == 'physics':
            mass = float(request.form.get('mass', 0))
            weight = mass * 9.8
            result = f"الفيزياء: الكتلة {mass}kg × 9.8 = {weight} نيوتن."

        # 2. منطق الرياضيات
        elif action == 'math':
            num = int(request.form.get('num', 0))
            result = f"الرياضيات: العدد {num} بالنظام الثنائي هو {bin(num)[2:]}"

        # 3. منطق الـ API للمصطلحات
        elif action == 'api':
            term = request.form.get('term')
            response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{term}")
            if response.status_code == 200:
                data = response.json()
                result = f"المصطلح {term}: {data[0]['meanings'][0]['definitions'][0]['definition']}"
            else:
                result = "عذراً، المصطلح غير موجود."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
    