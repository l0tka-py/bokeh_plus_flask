import os

from flask import Flask, render_template, request, jsonify
from bokeh.resources import INLINE

from crate_plot import *
from work_with_db import *


project_root = os.getcwd()
static_path = os.path.join(project_root, 'static\\')

app = Flask(__name__, static_folder=static_path)

path_to_json_file = R'.\db\Cars_80x.bokeh_cars.json'
js_obj = open_json_db(os.path.join(project_root, path_to_json_file))


# функция для отображения главной страницы
@app.route('/')
def homepage():

    if js_obj['status_code'] == 200:
        slice = create_slices_cars_price_id(js_obj['data'])
        script2, div2 = create_plot(slice)
    else:
        script2 = ""
        div2 = ""

    return render_template(
        template_name_or_list='./bokeh_exmp/index.html',
        script=script2,
        div=div2,
        js_resources=INLINE.render_js(),
        css_resources=INLINE.render_css()
    ).encode(encoding='UTF-8')


# функция для получения данных о машине
@app.route('/info_about_car/')
def get_info_about_car():
    car_id = request.values['id']

    info = info_about_car(js_obj['data'], car_id)

    return jsonify(info)


# функция для удаления данных о машине
@app.route('/delete_car/', methods=['POST'])
def delete_car_object():
    car_id = request.values['id']

    info = delete_car(path_to_json_file, js_obj['data'], car_id)

    return jsonify(info)


if __name__ == '__main__':
    app.run()
