FROM python:3.12-slim

WORKDIR /app

COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 8010

CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]