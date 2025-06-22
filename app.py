from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])  # Обработка главной страницы
def index():
    result = None
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])

        result = num1 + num2
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)  # Запуск сервера в режиме отладки