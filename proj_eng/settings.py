"""
Настройки Django для проекта proj_eng.

Сгенерировано с помощью 'django-admin startproject' в Django 4.1.7.

Для получения дополнительной информации о файле настроек смотрите
https://docs.djangoproject.com/en/4.1/topics/settings/

Полный список настроек и их значений можно найти по следующему адресу:
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Строим пути внутри проекта, например, BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Загружаем переменные окружения из файла .env
dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

# Быстрая настройка для разработки — не подходит для использования в продакшене
# См. https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# Секретный ключ для проекта. Он используется для криптографических операций
SECRET_KEY = str(os.getenv("SECRET_KEY"))

# Включение режима отладки. Включать только в разработке.
DEBUG = bool(os.getenv("DEBUG"))

# Разрешенные хосты — список хостов, с которых разрешено подключение к серверу
ALLOWED_HOSTS = ['*']

# Определение приложений, которые должны быть установлены в проекте
INSTALLED_APPS = [
    'django.contrib.admin',  # Административная панель Django
    'django.contrib.auth',  # Система аутентификации
    'django.contrib.contenttypes',  # Система контента
    'django.contrib.sessions',  # Сессии
    'django.contrib.messages',  # Сообщения
    'django.contrib.staticfiles',  # Статические файлы
]

# Промежуточное ПО (middleware), которое обрабатывает запросы
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Средства безопасности
    'django.contrib.sessions.middleware.SessionMiddleware',  # Сессии
    'django.middleware.common.CommonMiddleware',  # Общие настройки
    # 'django.middleware.csrf.CsrfViewMiddleware',  # Защита от CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Аутентификация
    'django.contrib.messages.middleware.MessageMiddleware',  # Сообщения
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Защита от кликджекинга
]

# Основной файл URL-ов
ROOT_URLCONF = 'proj_eng.urls'

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Используем DjangoTemplates для рендеринга
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')  # Путь к директории с шаблонами
        ],
        'APP_DIRS': True,  # Автоматически ищем шаблоны в каталогах приложений
        'OPTIONS': {
            'context_processors': [  # Контекст-процессоры для обработки данных в шаблонах
                'django.template.context_processors.debug',  # Отладочная информация
                'django.template.context_processors.request',  # Доступ к запросу
                'django.contrib.auth.context_processors.auth',  # Доступ к информации о пользователе
                'django.contrib.messages.context_processors.messages',  # Доступ к сообщениям
            ],
        },
    },
]

# Приложение WSGI для развертывания проекта
WSGI_APPLICATION = 'proj_eng.wsgi.application'

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Используем SQLite для базы данных
        'NAME': BASE_DIR / 'db.sqlite3',  # Путь к базе данных
    }
}

# Валидация паролей — набор проверок для паролей пользователей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Проверка на схожесть атрибутов
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Минимальная длина пароля
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Проверка на распространенные пароли
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Проверка на числовые пароли
    },
]

# Интернационализация и локализация
LANGUAGE_CODE = 'ru-ru'  # Устанавливаем русский язык
TIME_ZONE = 'UTC'  # Устанавливаем часовой пояс UTC
USE_I18N = True  # Включаем интернационализацию
USE_TZ = True  # Включаем работу с временными зонами

# Настройки статических файлов (CSS, JavaScript, изображения)
STATIC_URL = '/static/'  # URL для доступа к статическим файлам
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Путь к директории с собранными статическими файлами
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Путь к статическим файлам проекта
]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'  # Хранилище для статических файлов

# Тип поля для основного первичного ключа
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Используем BigAutoField для первичных ключей
