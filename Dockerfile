# Используем официальный образ Python
FROM python:3.12.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Открываем порт
EXPOSE 8000

# Запускаем сервер
CMD [gunicorn src.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000]
