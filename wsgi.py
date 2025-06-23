import os
from app import app as application   # импортируем ваше Flask-приложение как application

# Переменная application — это стандартная точка входа для WSGI-серверов.
# Ниже блок на случай прямого запуска через python wsgi.py (не обязателен в проде)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0', port=port)