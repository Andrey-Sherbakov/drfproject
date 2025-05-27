# Movies

**API** для хранения информации о фильмах написанный на **Django Rest Framework**

_Учебный проект в котором я изучал возможности DRF_

## Технологии

* Django Rest Framework
* PostgreSQL
* Simple JWT
* Docker

## Установка и запуск

1. Клонировать репозиторий:

```shell
git clone https://github.com/Andrey-Sherbakov/task_manager.git
cd task_manager
```

2. Изменить данные в файле .sample.env на свои и переименовать его в .env
3. Запустить docker compose:

```shell
docker compose up --build
```

4. Применить миграции:

```shell
docker compose exec drfproject python manage.py migrate
```

5. Создать суперпользователя:

```shell
docker compose exec drfproject python manage.py createsuperuser
```

_Теперь вам доступно API по адресу http://127.0.0.1:8000/api/v1/, админ
панель - http://127.0.0.1:8000/admin/ и adminer для работы с базой данных - http://127.0.0.1:8080/_
