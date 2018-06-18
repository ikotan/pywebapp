from bottle import debug
debug(True)

from bottle import route, run, template

@route('/')
def index():
    return template('templates/index.tpl')

@route('/abalone', method='POST')
def result():
    return template('templates/result.tpl',
                    sex='不明',
                    length=0,
                    diameter=0,
                    height=0,
                    weight=0,
                    age=0)

run(host='192.168.40.10', port=8888, reloader=True)
