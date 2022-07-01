# Тестовое для S7 IT

Задание выполнял на python3.10, но вроде как с typing'ом был аккуратен, так что
и с 3.7 должно работать

SQL запросы для выборки с фильтрацией по дате находятся в папке `ddl`

Чтобы запрос на выборку работал быстрее, нужно навешивать индексы на поля, по
которым планируется выборка

### Используемые библиотеки

- SQLAlchemy - многофункциональный ORM, все общение с БД через него
- Pydantic - многофункциональная валидация данных + сериализация/десериализация


- Стандартная библиотека - мощный набор инструментов на все случаи жизни

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd S7_interview
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```
или для пользователей Windows

```
source env/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить проект:
```
main.py
```
