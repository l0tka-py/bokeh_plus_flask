from bokeh import events
from bokeh.plotting import figure
from bokeh.layouts import column, row
from bokeh.embed import components
from bokeh.models import (Button, CustomJS, ColumnDataSource)


def create_plot(data_for_plot: dict) -> tuple:
    """
    Функция для построения графика
    data_for_plot: dict - словарь который содержит срезы с информацией о машинах 
            cars - производитель + часть айди (часть айди для обеспечения уникальности);
            price - цена машины в 1985году;
            id - уникальный идентификатор
    return (sctrip, div) - script - bokeh генерирует скрипт для отрисовки всех созданных элементов;
                           div - bokeh генерирует пустые div которые заполняет с помощью script
    """

    # ColumnDataSource является ядром большинства графиков
    # Можно передать списки price и cars в ручную, но использование
    # ColumnDataSource дает доп возможности для взаимодействия с графиком
    # в том числе и по web
    src = ColumnDataSource(
        data=dict(price=data_for_plot['price'],
                  cars=data_for_plot['cars'],
                  id=data_for_plot['id'])
    )

    # Подкласс Plot, который упрощает создание графиков
    main_plot = figure(
        x_range=data_for_plot['cars'],
        tools="tap",
        title="Самые дорогие машины за 1985 год",
        width=1400
    )

    # задаем параметры графику (ось x, y и прочие)
    main_plot.vbar(x='cars', top='price', source=src, width=0.6)
    main_plot.xgrid.grid_line_color = None
    main_plot.x_range.range_padding = 0
    main_plot.y_range.start = 0
    main_plot.xaxis.major_label_orientation = 1

    # создаем кнопку, которая будет вызывать отрисовку карточку выбранного объекта
    # очень важно обратить внимания на js_on_event, так как там происходит основная
    # магия, передаются основные объекты для взаимодействия с выбранным bar
    # а помогает в этом как раз ColumnDataSource (22 строка кода с описанием,
    # более подробно есть в документации)
    show_car_info_button = Button(
        label="Карточка объекта", button_type="success", min_width=130, min_height=30)
    show_car_info_button.js_on_event(events.ButtonClick,
                                     CustomJS(args=dict(src=src),
                                              code="""
                                                show_info(src.data.id, src.selected.indices[0])
                                                """)
                                     )

    # создаем кнопку, которая будет вызывать функцию для удаления выбранного объекта,
    # после они будут обновлены и график будет перестроен
    # очень важно обратить внимания на js_on_event так как там происходит основная
    # магия, передаются основные объекты для взаимодействия с выбранными данными
    # а помогает в этом как раз ColumnDataSource (22 строка кода с описанием,
    # более подробно есть в документации)
    # тут дополнительно передается объект графика, чтобы потом его можно было обновить,
    # для отрисовки новых элементов
    delete_car_button = Button(
        label="Удалить объект", button_type="success", min_width=130, min_height=30)
    delete_car_button.js_on_event(events.ButtonClick,
                                  CustomJS(args=dict(src=src, main_plot=main_plot),
                                           code="""
                                            delete_selected_car(main_plot, src, src.selected.indices[0]);
                                            """)
                                  )

    # создаем лэйаут кнопок для отображения информации о выбранной машине,
    # и удаление выбранной машины, находятся на одной строчке
    button_row = row([show_car_info_button, delete_car_button])
    # создаем общий лейаут для графика и кнопок (будут отображены
    # в порядке расположения в списке)
    plot_and_button = column([main_plot, button_row])

    # возвращает tuple для отрисовки всего на клиентской стороне
    return components(plot_and_button)
