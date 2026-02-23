FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT=8000
ENV DJANGO_SETTINGS_MODULE=project_yaa123122.settings

WORKDIR /app

# Встановлюємо системні залежності (потрібні для pillow)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копіюємо залежності
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо проєкт
COPY . /app/

# Збираємо статичні файли
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Запускаємо Gunicorn


CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn project_yaa123122.wsgi:application --bind 0.0.0.0:$PORT"]