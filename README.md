# bokeh_plus_flask
Проект реализован с помощью библиотек bokeh и flask. Версия PYTHON 3.11.4.  

## Задание
* Создать веб-приложение для интерактивной визуализации данных (графов). В качестве основного фреймворка предлагается использовать библиотеку Bokeh (Python). 
В качестве основы/базы приложения и тестовых данных можно использовать готовые модели от разработчика или из любых других открытых источников.
Для пользовательской веб-схемы отображения графа реализовать следующие функции: 
1. Добавить кнопку на схему «Карточка», которая открывает карточку ранее выделенного мышью узла со всеми его данными (атрибутами).
2. Карточку можно отобразить как отдельное pop-up окно (кроме всплывающей подсказки), на отдельной странице или вывести ее содержимое ниже под интерактивной схемой.  
3. Добавить кнопку на схему «Удалить», выполняющую соответствующее действие для выбранного узла. Удаление узла происходит на схеме и в данных,  
перезагрузка схемы (обновление станицы) учитывает отсутствие ранее удаленных узлов. *  

## Для запуска у себя
Нужно:
1) Установить интерпитатор Python (https://wiki.python.org/moin/BeginnersGuide/Download);
2) Скачать этот проект (https://skillbox.ru/media/code/instruktsiya-kak-skachat-fayl-s-github/) и разархивировать его в любую удобную папку;  
3) Перейти в папку проекта и создать виртуальное окружение (https://habr.com/ru/articles/491916/);  
4) Активировать виртуальное окружение (venv\Scripts\activate.bat - для Windows; source venv/bin/activate - для Linux и MacOS);  
5) Командой "pip install -r requirements.txt" установить все необходимые библиотеки;  
(на самом деле требуется установить только bokeh и flask, все библиотеки указынные в requirements.txt  
устанавливаются как зависимости от bokeh и flask)  
6) Запустить main.py с помощью интерпритатора python (https://pythonru.com/osnovy/zapusk-python-i-python-skript-na-kompjutere);  
7) Открыть браузер по адресу http://127.0.0.1:5000/ (https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html);  
8) Тестировать приложение :)

## Состав приложения
|-main.py - Главный исполняемый скрипт;  
|-requirments.txt - список зависимостей;  
|--templates/bokeh_exmp/index.html - главный html файл проекта;  
|--static/bokeh_exmp/css/main.css - главный файл стилей;  
|--static/bokeh_exmp/js/main.js - главный исполняемый js файл, в нем происходит работа с объектами графика;  
|--static/bokeh_exmp/js/jquery.min.js - jquery;  
|--sub_programs/create_plot.py - главный файл где инициализируется график;  
|--sub_programs/work_with_db.py - файл для работы с бд;  
|--db/Cars_80x.bokeh_cars.json - файл бд (изначально использовал mongo.db, но подумал что будет не удобно для быстрой  
проверки и в итоговом скрипте оставил только работу с json).  

## Пример работы
Все скриншоты доступны по ссылке - https://github.com/l0tka-py/images/tree/eabacda4479642b64784dc346f4ff93a26d682c6  

### Открываем окно браузера:
![img1](https://github.com/l0tka-py/images/blob/master/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-14%20000627.png)  
### Выбор объекта и отображение его карточки
![img2](https://github.com/l0tka-py/images/blob/master/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-14%20000710.png)
![img3](https://github.com/l0tka-py/images/blob/master/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-14%20000742.png])
### Удаление объекта
![img4](https://github.com/l0tka-py/images/blob/master/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-14%20000916.png)
![img5](https://github.com/l0tka-py/images/blob/master/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-14%20001552.png)
