# API для Yatube

## Описание
REST API для социальной сети Yatube. Позволяет создавать посты, комментарии, подписываться на авторов.

## Установка

```bash
git clone https://github.com/sofitrutnewa/api-final-yatube-ad.git
cd api-final-yatube-ad
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd yatube_api
python manage.py migrate
python manage.py runserver
```

## Документация
http://127.0.0.1:8000/redoc/
