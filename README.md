# Репозиторий для представления результатов разработки для ВКР

## Используемый стек

**Язык программирования:** Python

**Основные используемые библиотеки:** Flask, Pandas, Numpy, nltk, scrapy

**БД:** MySql

**Web-cервер:** Nginx

## Описание функциональных возможностей

Для демонстрации работы предобученной [модели](https://colab.research.google.com/drive/1BsP6crvOYPihdtJ_rIx7KEms7z6nm0UE) был разработан сайт.

На сайте пользователь может ознакомиться с вакансиями, отфильтровать их по [ключевым навыкам и/или профессиональным сферам](#навыки-и-профессиональные-сферы). Авторизованный пользователь может добавить заинтересовавшие вакансии в избранное.

Так же авторизованнй пользователь может указать свои навыки в личном кабинете и сразу посмотреть подхоящие ему вакансии.

## Инструкция по запуску

- Склонируйте репозиторий

```cmd
git clone https://github.com/4ertovo4ka/vkr.git
```

- В папке проекта создайте виртуальное окружение и перейдите в него

```cmd
python -m venv .venv

source .venv/bin/activate
```

- Установите необходимые для работы пакеты

```cmd
pip install pipenv

pipenv install
```

- Переместите из корня проекта в папку webapp файл .rename.env и переименуйте его в .env
- В данном файле заполните необходимые данные

- Запустите sql скрипт из папки demo_data. Дождитесь пока все данные будут перенесены в базу

- Запустите flask

```cmd
vkr/backend > flask --app webapp run
```

Сервер будет запущен по адресу [127.0.0.1:5000](http://127.0.0.1:5000)

## Навыки и профессиональные сферы

**Специализации:**

- Bigdata
- Development
- DevOps
- QA
- System administration
- Teaching
- Teamlead

**Языки программирования:**

- Python
- Java
- PHP
- Pascal
- Ruby
- ABAP
- JavaScript
- C++
- SQL
- Delphi
- TypeScript
- .NET
- Kotlin
- Scala

**Базы данных:**

- MySQL
- PostgreSQL
- Redis
- Cassandra
- Prometheus
- InfluxDB
- MongoDB
- MariaDB
- CouchDB
- ClickHouse

**Фреймворки:**

- Django
- Flask
- AIOHTTP
- Falcon
- Spark

**Веб-протоколы:**

- TCP/IP
- TCP
- WebSocket

**Поисковые системы:**

- Elasticsearch
- Solr
- Sphinx

**Веб-серверы:**

- Tornado
- Apache
- Nginx

**Брокеры сообщений:**

- RabbitMQ
- Kafka
- Amazon SQS

**Операционные системы:**

- Windows
- Linux
- Debian

**Контроль версий:**

- Git
- Bitbucket
- Github
- Mercurial

**Виртуализация:**

- Docker
- VMware

**Автоматизация:**

- PowerShell
- Ansible
- Jenkins
- TeamCity

**ORM:**

- Sqlalchemy
- Mongoengine
- Hibernate

**Системы управление проектами:**

- Redmine
- Confluence

**Методы управления проектами:**

- Scrum
- Kanban
- Agile

**Системы мониторинга:**

- Zabbix
