
FROM mcr.microsoft.com/playwright/python:v1.56.0-noble

WORKDIR /app

ENV PYTHONPATH=/app

RUN mkdir -p /app/artifacts

RUN ln -s /app/artifacts/ui.log /app/ui.log

# Копируем зависимости
COPY requirements .

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements

# Устанавливаем Google Chrome
RUN playwright install chrome

# Копируем проект
COPY . .

# Запускаем тесты
CMD ["pytest", "-v"]
