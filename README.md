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

## Результаты
- ![Screenshot_2024-03-29_19-09-00](https://github.com/Elianess/docker-3-containers/assets/66972306/551d90ef-bef7-4a74-9665-53791586a982)
- ![Screenshot_2024-03-29_19-02-05](https://github.com/Elianess/docker-3-containers/assets/66972306/50baf201-693e-4369-ac83-e6105bec27e2)
- ![Screenshot_2024-03-29_19-04-59](https://github.com/Elianess/docker-3-containers/assets/66972306/caf7d2e9-116f-430c-8a70-e158c64c9ff3)
- ![Screenshot_2024-03-29_19-06-17](https://github.com/Elianess/docker-3-containers/assets/66972306/81947913-a59b-4bf3-8812-00cefa84bf05)




