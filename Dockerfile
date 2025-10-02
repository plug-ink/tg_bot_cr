FROM python:3.13-slim

# Ставим системные зависимости
RUN apt-get update && apt-get install -y \
    gcc g++ build-essential libzbar0 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY . .

# Запуск
CMD ["python3", "bot.py"]