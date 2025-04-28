from flask import Flask, render_template_string, request

app = Flask(__name__)

# Список для хранения товаров в корзине
cart = []

# HTML шаблон для страницы интернет-магазина
html_template = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Интернет-магазин</title>
</head>
<body>
    <h1>В будущем вы сможете здесь приобрести что-нибудь необходимое вам!</h1>
    <!-- Остальной HTML-код -->
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

# Остальные маршруты...

if __name__ == '__main__':
    app.run(debug=True)