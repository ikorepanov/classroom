# Classroom
## Описание
Проект по созданию удобного приложения, которое позволяет учителю генерировать рассадку учеников по новым местам в классе.  

## Содержание
1. [Как запустить проект](#как-запустить-проект)
2. [Стек технологий](#стек-технологий)
3. [Автор, контакты](#авторы-контакты)

## Как запустить проект
В дальнейших командах используйте `python3` вместо `python` - **для Linux и macOS**.   
- клонируйте репозиторий:
  ```
  git clone git@github.com:ikorepanov/classroom
  ```
- перейдите в папку с проектом:
  ```
  cd classroom
  ```
- разверните виртуальное окружение:
  ```
  python -m venv venv
  ```
- активируйте виртуальное окружение:
  * команда для Windows
    ```
    source venv/Scripts/activate
    ```
  * команда для Linux и macOS
    ```
    source venv/bin/activate
    ```
- обновите `pip`:
  ```
  python -m pip install --upgrade pip
  ```
- установите зависимости:
  ```
  pip install -r requirements.txt
  ```
- перейдие в папку `classroom`:
  ```
  cd classroom
  ```
- выполните миграции:
  ```
  python manage.py migrate
  ```
- создайте суперпользователя:
  ```
  python manage.py createsuperuser
  ```
- запустите сервер разработчика:
  ```
  python manage.py runserver
  ```
Проект будет доступен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).  
Админка проекта: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).  
Для доступа - использовать данные суперпользователя, созданные ранее.  

## Стек технологий
- Python 3.9
- Django 4.2
- HTML
- CSS
- Bootstrap

## Автор, контакты
- Илья Корепанов  
[![Telegram Badge](https://img.shields.io/badge/Telegram-blue?style=social&logo=Telegram)](https://t.me/number_one_lobster) [![Gmail Badge](https://img.shields.io/badge/Gmail-red?style=social&logo=Gmail)](mailto:ikorepanov.study@gmail.com)   
