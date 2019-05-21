import os

import waitress
from flask import Flask, render_template, request, url_for, redirect

from app.lib import which_profession


def start():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/news')
    def news():
        return render_template('news.html')

    @app.route('/goods')
    def goods():
        return render_template('goods.html')

    @app.route('/tests')
    def tests():
        return render_template('tests.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/java')
    def java():
        return render_template('java.html')

    @app.route('/python')
    def python():
        return render_template('python.html')

    @app.route('/csharp')
    def csharp():
        return render_template('csharp.html')

    @app.route('/1c')
    def one_c():
        return render_template('1c.html')

    @app.route('/test_prof')
    def test_with_form():
        in_ex = request.args.get('in_ex')
        sen_int = request.args.get('sen_int')
        think_feel = request.args.get('think_feel')
        judg_perc = request.args.get('judg_perc')

        if in_ex and sen_int and think_feel and judg_perc:
            total = which_profession(str(in_ex), str(sen_int), str(think_feel), str(judg_perc))
            return render_template('test_py.html', total=total, in_ex=in_ex, sen_int=sen_int, think_feel=think_feel,
                                   judg_perc=judg_perc)

        return render_template('test_py.html')

    print(os.getenv('APP_ENV'))
    print(os.getenv('PORT'))
    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)


if __name__ == '__main__':
    start()
