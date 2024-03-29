В данном проекте используется Docker Compose для создания и управления тремя контейнерами: базой данных `PostgreSQL`, приложением `Flask` и сервером `Nginx`.

## project structure:
```
├── flask
│   ├── Dockerfile
│   ├── requirements.txt
│   └── server.py
├── db
│   ├── data.txt 
│   └── init.sql
├── nginx
│   └── nginx.conf
├── compose.yaml
└── README.md
```

## База данных PostgreSQL
В контейнер монтируются два тома: 
- один для хранения данных базы данных
- другой для инициализации базы данных скриптом init.sql.

В скрипте `init.sql` создается таблица mytable с двумя столбцами: `id` и `name`, и заполняется данными из файла `data.txt`.
Для подключения к бд используется библиотека `psycopg2-binary`.

## Приложение Flask
Контейнер приложения Flask строится на основе образа `python:3.9-slim-buster`. В `Dockerfile` устанавливаются необходимые пакеты Flask и Werkzeug, а также копируется код приложения. Приложение настроено для подключения к базе данных `PostgreSQL` через URL-адрес, указанный в переменной окружения `DATABASE_URL`.
Все необходимые зависимости для приложения указаны в файле `requirements.txt`.

## Сервер Nginx
В контейнер монтируется файл конфигурации `nginx.conf`, в котором настраивается обратный прокси-сервер для перенаправления запросов на приложение Flask.

## резульат
- ![Screenshot_2024-03-29_19-06-17](https://github.com/Elianess/docker-3-containers/assets/66972306/e46e5bce-83fb-454e-8256-7d85fe1d4aad)
- ![Screenshot_2024-03-29_19-02-05](https://github.com/Elianess/docker-3-containers/assets/66972306/5b055fdf-2ea1-4e3d-99af-5e0b44222df3)
- ![Screenshot_2024-03-29_19-04-59](https://github.com/Elianess/docker-3-containers/assets/66972306/876e2d4a-5d12-42c8-8569-20934cdccc96)
- ![Screenshot_2024-03-29_19-06-17](https://github.com/Elianess/docker-3-containers/assets/66972306/0f6a5857-f877-4cbc-8bc9-deee3c1d616f)



