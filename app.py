from bottle import debug
debug(True)
from bottle import (default_app, route, run, template, request, HTTPError)
from abalone_predictor import AbalonePredictor
from collections import namedtuple
from bokeh.plotting import figure
from bokeh.embed import components

READABLE_SEX = ['メス', '不明', 'オス']

INPUT_DATA = ('sex', 'length', 'diameter', 'height', 'weight')

BaseAbalone = namedtuple('BaseAbalone', INPUT_DATA + ('age', ))


class Abalone(BaseAbalone):
    @property
    def sex_str(self):
        return READABLE_SEX[int(self.sex)]


@route('/')
def index():
    return template('templates/index.tpl')


@route('/abalone', method='POST')
def result():
    try:
        age = calc_age(**request.params)
        abalone = Abalone(age=age, **request.params)
    except (KeyError, ValueError) as e:
        raise HTTPError(status=400, body=e)
    script, div = get_graph(abalone)
    return template(
        'templates/result.tpl', abalone=abalone, script=script, graph=div)


_predictor = AbalonePredictor()


def calc_age(sex, length, diameter, height, weight):
    age = _predictor.predict(
        int(sex), int(length), int(diameter), int(height), int(weight))
    return float(age)


def get_graph(abalone):
    p = figure(plot_width=400, plot_height=400, title='実年齢と推定値の分布')
    p.xaxis.axis_label = '実年齢'
    p.yaxis.axis_label = '推定値'
    p.line([0, 30], [0, 30], line_dash='dotted', legend='実年齢と推定値が一致するライン')
    p.circle(_predictor.y_train, _predictor.prediction, legend='訓練データにおける分布')
    p.line(
        [0, 30], [abalone.age, abalone.age],
        legend='捕まえたアワビの推定年齢',
        color="green")
    p.legend.location = 'top_left'
    p.legend.click_policy = 'mute'
    script, div = components(p)
    return script, div

application = default_app()

#  run(host='192.168.40.10', port=8888, reloader=True)
