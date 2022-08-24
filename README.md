## Описание
Пет проект с правильной архитектурой приложения (Blueprints, слой DAO, слой Services, отдельные views в неймспейсах, Модели, Схемы, Серриализация, Десерриализация, Class Based Views, Авторизация).

Таблицы: Фильмы - Жанры - Режиссеры

Стек: Flask + RESTx + SQLAlchemy + Marshmallow + JWT.

### Требования к ПО
- Python 3.10

### Установка и запуск
1. Создать и активировать виртуальное окружение
```bash
python -m venv venv

source venv/bin/activate
```

2. Установить зависимости
```bash
pip install -r requirements.txt
```

3. Запускаем проект

 - Объявляем переменные окружения
```bash
export PROJECT_DIR=/path_to_project/skypro_hw_18
export PYTHONPATH=$PROJECT_DIR
export FLASK_APP=run     
export FLASK_ENV=development   
```
- Производим первичную инициализацию базы данных
```bash
python blueprints/movie/db/db_init.py

>> Database initialized successfully
```
- Запускаем веб сервер
```bash
python flask run
```
4. Примеры запросов
```bash
Получить токен по логину и паролю

POST http://127.0.0.1:5000/auth
{
	"username": "ivan",
	"password": "qwerty",
}
```

```bash
Создать пользователя

POST http://127.0.0.1:5000/users
Authorization: Bearer token_here
{
	"username": "ivan",
	"password": "qwerty",
	"role": "admin"
}
```

```bash
Получить список фильмов

GET http://127.0.0.1:5000/movies/
Authorization: Bearer token_here
```

```bash
Удалить жанр

DELETE http://127.0.0.1:5000/genres/5/
Authorization: Bearer token_here
```
...

## Задание

В этом задании вам нужно будет написать проект для онлайн-кинотеатра, разложив его по папочкам и слоям.

### Шаг 1. Используйте репозиторий с архитектурой проекта

Скопируйте структуру и заготовки из репозитория заготовки (https://github.com/skypro-008/flask-hard-blank).

Установите зависимости и убедитесь, что всё работает. Теперь вы готовы писать проект!

### Шаг 2. Создайте представления

Используя Flask-RESTX, создайте три неймспейса и отдельные папки под них. Пропишите соответствующие методы.

**Для фильмов**

- [ ]  Получение по id
- [ ]  Получение всех
- [ ]  Добавление
- [ ]  Изменение
- [ ]  Удаление

**Для режиссеров**

- [ ]  Получение по id
- [ ]  Получение всех

**Для жанров**

- [ ]  Получение по id
- [ ]  Получение всех

Создайте Class-Based Views и напишите методы, которые возвращали бы пустые строки или какие-то рандомные данные. Запустите приложение и, используя Postman, убедитесь, что всё работает.

### Шаг 3. Создайте модели

**Фильм** (Movie)

- [ ]  id
- [ ]  title
- [ ]  description
- [ ]  trailer
- [ ]  year
- [ ]  rating
- [ ]  genre_id (связь с Genre)
- [ ]  director_id (связь с Director)

**Жанр** (Genre)

- [ ]  id
- [ ]  name

**Режиссер** (Director)

- [ ]  id
- [ ]  name

### Шаг 3.1. Наполните БД

Создайте объекты фильмов, жанров и режиссеров и сохраните их в БД.

**Или** в приложении для работы с БД (например, DBeaver) или в плагине к PyCharm для работы с БД создайте строки в таблице — наполните БД.

### Шаг 4. Напишите схемы сериализации

Напишите схемы сериализации для Movie, Genre, Director и разместите их там, где предусмотрено архитектурой. 

### Шаг 5. Напишите DAO

Напишите объекты доступа к данным для трех моделей.

**Фильм** (Movie)

- [ ]  Получить все фильмы
- [ ]  Получить фильм по id
- [ ]  Получить все фильмы режиссера
- [ ]  Получить все фильмы жанра
- [ ]  Получить все фильмы за год
- [ ]  Создать фильм
- [ ]  Изменить информацию о фильме
- [ ]  Удалить фильм

**Режиссер** (Director)

- [ ]  Получить всех режиссеров
- [ ]  Получить по id

**Жанр** (Genre)

- [ ]  Получить все жанры
- [ ]  Получить по id

### Шаг 6. Напишите сервисы

Теперь, когда все методы работы с данными подготовлены, пора браться за бизнес-логику. Напишите код для трех сервисов, используя DAO.

**Для фильмов**

- [ ]  Добавление фильма
- [ ]  Получение фильма
- [ ]  Получение всех фильмов
- [ ]  Изменение фильма
- [ ]  Фильтрация фильма по разным полям
- [ ]  Удаление фильма

**Для режиссеров**

- [ ]  Получение всех
- [ ]  Получение по id

**Для жанров**

- [ ]  Получение всех
- [ ]  Получение по id

### Шаг 7. Допишите код **views** с использованием сервисов

**Допишите код views жанров:**

- [ ]  GET /genres — получить все жанры.
- [ ]  GET /genres/3 — получить жанр по ID.

**Допишите код views режиссеров:**

- [ ]  GET /directors — получить всех режиссеров.
- [ ]  GET /directors/3 — получить режиссера по ID.

**Допишите код views фильмов:**

- [ ]  GET /movies — получить все фильмы.
- [ ]  GET /movies/3 — получить фильм по ID.
- [ ]  GET /movies?director_id=15 — получить все фильмы режиссера.
- [ ]  GET /movies?genre_id=3 — получить все фильмы жанра.
- [ ]  GET /movies?year=2007 — получить все фильмы за год.
- [ ]  POST /movies — создать фильм.
- [ ]  PUT /movies/1 — изменить информацию о фильме.
- [ ]  DELETE /movies/1 — удалить фильм.

### Шаг 8. Создайте пользователя

Создайте модель и схему пользователя и добавьте к ней CRUD (views с методами `GET/POST/PUT`). 

Описание модели пользователя:

```python
class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String)
	password = db.Column(db.String)
	role = db.Column(db.String)
```

### Шаг 8.1. Добавьте методы генерации хеша пароля пользователя

Хешируем пароли с помощью `pbkdf2_hmac`.

```python
config.py

# Добавляем константы в файл constants.py
PWD_HASH_SALT = b'secret here'
PWD_HASH_ITERATIONS = 100_000

# services/user.py, class UserService для сложной архитектуры
# models.py, class User для простой архитектуры

# Метод хеширование пароля
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

def get_hash(password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
```
### Шаг 9. Добавьте эндпоинты аутентификации

`POST` /auth/ — возвращает `access_token` и `refresh_token` или `401` - Anonymous (кто угодно)

`PUT` /auth/ — возвращает `access_token` и `refresh_token` или `401` - Anonymous (кто угодно)


`POST /auth` — получает логин и пароль из Body запроса в виде JSON, далее проверяет соотвествие с данными в БД (есть ли такой пользователь, такой ли у него пароль)
и если всё оk — генерит пару access_token и refresh_token и отдает их в виде JSON.

`PUT /auth` — получает refresh_token из Body запроса в виде JSON, далее проверяет refresh_token и если он не истек и валиден — генерит пару access_token и refresh_token и отдает их в виде JSON.

### **Шаг 10. Ограничьте доступ на чтение**

Защитите (ограничьте доступ) так, чтобы к некоторым эндпоинтам был ограничен доступ для запросов без токена. Для этого создайте декоратор `auth_required` и декорируйте им методы, которые нужно защитить.

`GET` /directors/ + /directors/id - Authorized Required

`GET` /movies/ + /movies/id - Authorized Required

`GET` /genres/ + /genres/id - Authorized Required

### Шаг 11. Ограничьте доступ на редактирование

Защитите (ограничьте доступ) так, чтобы к некоторым эндпоинтам был доступ только у администраторов ( `user.role == admin` ) Для этого создайте декоратор `admin_required` и декорируйте им  методы, которые нужно защитить.

`POST/PUT/DELETE`  /movies/ + /movies/id - Authorized Required + Role admin Required

`POST/PUT/DELETE`  /genres/ + /genres/id - Authorized Required + Role admin Required

`POST/PUT/DELETE`  /directors/ + /directors/id - Authorized Required + Role admin Required

### Шаг 7. Добавьте регистрацию пользователя

`POST` /users/ — создает пользователя - Anonymous (кто угодно)

Пример запроса:
```
POST /users/

{
	"username": "ivan",
	"password": "qwerty",
	"role": "admin"
}
```

### Шаг 8. Создайте  пользователей в БД

Создайте пользователей в БД — двух обычных и одного администратора.

Для простой архитектуры:

Добавьте в app.py этот кусок кода и вызовите функцию `create_data` в `register_extensions`.

```python
def create_data(app, db):
    with app.app_context():
        db.create_all()

        u1 = User(username="vasya", password="my_little_pony", role="user")
        u2 = User(username="oleg", password="qwerty", role="user")
        u3 = User(username="oleg", password="P@ssw0rd", role="admin")

        with db.session.begin():
            db.session.add_all([u1, u2, u3])
```

---
[SkyPro](https://sky.pro) - [Python Developer](https://sky.pro/courses/programming/python-web-course)
