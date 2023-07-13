import os
import json


def open_json_db(file_path: str) -> dict:
    """
    Функция для открытия базы данных (json файла) с данными о машинах, которые были выпущены в 1985 году
    file_path: str - путь до json файла
    return: возвращает в случае удачного выполнения код 200 и данные из файла бд,
           если не удалось открыть бд, по причине отсутствия файла, возвращает код 500 - ошибка сервера
    """
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return {'status_code': 200, 'data': data}
    else:
        return {'status_code': 500}


def save_to_json_db(file_path: str, data) -> dict:
    """
    Функция для сохранения данных в файл бд
    file_path: str - путь до json файла
    data объект для записи в БД
    return: возвращает в случае удачного выполнения код 200,
           если не удалось открыть бд, по причне отсутвия файла, возвращает код 500 - ошибка сервера
    """
    if os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)
        return {'status_code': 200}
    else:
        return {'status_code': 500}


def get_expensive_cars_from_json(data_cars: list, lim: int = 10) -> list:
    """
    Функция для работы с словарем, полученным из json файла,
    сортирует и выдает самые дорогие машины выпущенные за 1985год
    data_cars: list - список с данными по машинам
    lim: int - возвращаемое кол-во машин
    return: - возвращает срез самых дорогих машин
    """
    data_cars.sort(key=lambda data_cars: data_cars['price'], reverse=True)
    return data_cars[:lim]


def get_cheap_cars_from_json(data_cars: list, lim: int = 10) -> list:
    """
    Функция для работы с словарем, полученным из json файла,
    сортирует и выдает самые дешевые машины выпущенные за 1985год
    data_cars: list - список с данными по машинам
    lim: int - возвращаемое кол-во машин
    return: - возвращает срез самых дешевых машин
    """
    data_cars.sort(key=lambda data_cars: data_cars['price'])
    return data_cars[:lim]


def info_about_car(data_cars: list, id: str) -> dict:
    """
    Получение информации о машине по ее id
    data_cars: list - список с данными по машинам
    id: str - строка с id искомой машины
    return: возвращает словарь с кодом выполнения операции и информацией о машине,
           если машина не найдена, возвращает код 400
    """
    for car in data_cars:
        # проверка на совпадение id который пришел из запроса
        # и id в описании объекта
        if car['_id']['$oid'] == id:
            return {'status_code': 200, 'info_about_car': car}
    return {'status_code': 400}


def delete_car(file_path: str, data_cars: list, id: str) -> dict:
    """
    Удаляет информацию о машине из всех источников (на диске и в озу)
    file_path: str - путь до сохраняемого файла
    data_cars: list - список с данными по машинам
    id: str - строка с id искомой машины
    return: в случае успешного выполнения операции возвращает ststus_code == 200
           и данные для обновления графика, если на каком то из этапов произошла ошибка,
           возвращает status_code ошибки (400, 500)
    """

    # ищем объект в бд (озу) и проверяем ststus_code чтобы понимать нашли или нет
    deleted_object = info_about_car(data_cars, id)
    if deleted_object['status_code'] != 400:
        # удаляем полученный объект
        data_cars.remove(deleted_object['info_about_car'])
        # сохраняем в бд на диске результат
        status_code = save_to_json_db(file_path, data_cars)['status_code']
        # проверяем статус выполнения запроса и если все успешно,
        # формируем новые данные для отрисовки
        if status_code == 200:
            result_dict = create_slices_cars_price_id(data_cars)
            result_dict['status_code'] = status_code
            return result_dict
        else:
            return {'status_code': status_code}
    else:
        return {'status_code': deleted_object['status_code']}


def create_slices_cars_price_id(data_cars: list, lim: int = 10) -> dict:
    """
    Функция создает срез данных для их дальнейшего отображения на графике
    data_cars: list - список объектов с информацией о машинах
    lim - возвращаемое кол-во машин
    return: dict возвращаем словарь списков
    """
    # получаем самые дорогие машины
    exp_cars = get_expensive_cars_from_json(data_cars, lim)

    # с помощью list comprehension создаем необходимую информацию
    # (cars_mark - уникальные имена (на выбранном типе графика названия bar должны быть уникальны))
    # так что присоединяю последние несколько значений id - что и гарантирует уникальность :)
    cars_mark = [car['make'] + '\n' + car['_id']['$oid'][-3:]
                 for car in exp_cars]
    # цена автомобиля
    price = [car['price'] for car in exp_cars]
    # id автомобиля для дальнейшего взаимодействия с ним через WEB и в БД
    obj_id = [car['_id']['$oid'] for car in exp_cars]

    return {'cars': cars_mark, 'price': price, 'id': obj_id}
