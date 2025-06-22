from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_wbgt_risk(Tnw, Tg, Ta, work_intensity):
    try:
        # Преобразуем значения в числа
        Tnw = float(Tnw)
        Tg = float(Tg)
        Ta = float(Ta)
        intensity_value = float(work_intensity)
        
        # Рассчитываем WBGT
        wbgt = 0.7 * Tnw + 0.2 * Tg + 0.1 * Ta
        
        # Определяем уровень риска
        if wbgt <= intensity_value:
            return {
                "wbgt": round(wbgt, 1),
                "risk": "Низкий",
                "message": "Работа безопасна при условии наличия питьевой воды и наблюдения."
            }
        elif wbgt <= intensity_value + 2:
            return {
                "wbgt": round(wbgt, 1),
                "risk": "Умеренный",
                "message": "Требуется режим работы/отдыха (напр., 50% работы, 50% отдыха в час). Обильное питье!"
            }
        else:
            return {
                "wbgt": round(wbgt, 1),
                "risk": "Высокий/Опасный",
                "message": "Немедленно прекратить работу! Высокий риск теплового удара."
            }
            
    except (ValueError, TypeError):
        return None

@app.route('/', methods=["GET", "POST"])
def index():
    result = None
    error = None
    
    if request.method == "POST":
        # Получаем данные из формы
        water = request.form.get('water')
        black = request.form.get('black')
        air = request.form.get('air')
        intensity = request.form.get('intensity')
        
        # Проверяем, что все поля заполнены
        if not all([water, black, air, intensity]):
            error = "Пожалуйста, заполните все поля формы!"
        else:
            # Вычисляем результат
            result = calculate_wbgt_risk(water, black, air, intensity)
            if not result:
                error = "Ошибка в расчетах! Проверьте введенные данные."
    
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)