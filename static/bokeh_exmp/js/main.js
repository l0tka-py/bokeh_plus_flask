let current_bar_index = -1;

// ajax функция для отображения данных о машине
// открывает popup окно, показывает актуальные данные
function show_info(src, bar_index) {
    // проверяем выбран ли объект

    if (typeof bar_index != "undefined" && bar_index != null) {
        // чтобы не отправить повторно запрос, если объект уже
        // был отображен, проверяем повторное отображение с помощью
        // current_bar_index
        if (current_bar_index != bar_index) {

            current_bar_index = bar_index;
            // формируем данные для отправки на сервер
            car_id = { 'id': src[current_bar_index] };

            $.ajax({
                type: "GET",
                url: "info_about_car/",
                dataType: "json",
                data: car_id,
                success: function (response) {
                    // проверяем состояние ответа и в случаем успеха заполняем
                    // карточку
                    console.log(response);
                    if (response.status_code == 200) {
                        $('.car_creator').text(response.info_about_car["make"]);
                        $('.body-style').text(response.info_about_car["body-style"]);
                        $('.horsepower').text(response.info_about_car["horsepower"]);
                        $('.drive-wheels').text(response.info_about_car["drive-wheels"]);
                        $('.price').text(response.info_about_car["price"]);
                        $('.container.car').show();
                    }
                    else {
                        window.alert("Не удалось получить данные с сервера!")
                        console.log(response.status_code)
                    }
                }
            });
        }
        else {
            $('.container.car').show();
        }
    }
    else {
        window.alert("Выберете объект для отображения!");
    }
}

// функция обработчик закрытия карточки клиента
function close_info() {
    $('.container.car').hide();
}

// ajax функция для удаления данных о машине
// открывает popup окно, показывает актуальные данные
function delete_selected_car(updated_plot, src, del_index) {
    console.log(src.selected.indices);
    if (typeof del_index != "undefined" && del_index != null) {
        // формируем данные для отправки на сервер
        car_id = { 'id': src.data.id[del_index] };

        $.ajax({
            type: "POST",
            url: "delete_car/",
            dataType: "json",
            data: car_id,
            success: function (response) {
                if (response.status_code == 200) {
                    const indices = []
                    // Заполняем объект ColumnDataSource (описан в файле crate_plot)
                    // новыми данными, которые пришли с сервера
                    src.data.cars = response.cars;
                    src.data.price = response.price;
                    src.data.id = response.id;

                    //обновляем надписей оси x
                    updated_plot.x_range.factors = src.data.cars;
                    //функции для обновления данных ColumnDataSource и графика
                    //сбрасываем выбранный объект у ColumnDataSource
                    src.selected.indices = indices;
                    src.change.emit();
                    //сбрасываем выбранный объект у графика
                    updated_plot.indices = indices;
                    updated_plot.change.emit();
                    current_bar_index = -1;
                }
                else {
                    window.alert("Не удалось удалить объект");
                    console.log(response);
                }

            }
        });
    }
    else {
        window.alert("Выберете объект который нужно удалить!");
    }
}