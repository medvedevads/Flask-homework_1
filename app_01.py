from flask import Flask, render_template

app = Flask(__name__)


@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)

@app.route('/clothes/')
def clothes():
    title = {'title': 'Категории одежды'}
    _clothes = [
    {"name": "Футболка", "price": 1000, "descr": "Классическая белая футболка"},
    {"name": "Джинсы", "price": 2000, "descr": "Черные джинсы прямого кроя"},
    {"name": "Платье", "price": 3000, "descr": "Платье вечернее праздничное"}
]
    return render_template('product.html', **title, products = _clothes)

@app.route('/shoes/')
def shoes():
    title = {'title': 'Категории обуви'}
    _shoes = [{"name": "Кроссовки", "price": 1500, "descr": "Спортивные кроссовки для бега"},
              {"name": "Тюфли", "price": 2500, "descr": "Классические черные туфли"},
              {"name": "Сланцы", "price": 800, "descr": "Пляжные сланцы"}
]
    return render_template('product.html', **title, products = _shoes)

@app.route('/jackets/')
def jackets():
    title = {'title': 'Категории верхней одежды'}
    _jackets = [{"name": "Ветровка", "price": 7000, "descr": "Легкая ветровка"},
              {"name": "Пуховик", "price": 15000, "descr": "Теплый пуховик (до -30°C)"},
              {"name": "Пальто", "price": 9000, "descr": "Пальто из непромокаемого материала"}
]
    return render_template('product.html', **title, products = _jackets)

if __name__ == '__main__':
    app.run(debug=True)
