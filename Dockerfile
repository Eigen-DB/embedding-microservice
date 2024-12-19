FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN pip3 install -r requirements.txt

EXPOSE 8000

#CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]