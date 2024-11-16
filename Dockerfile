FROM python:3

WORKDIR /app

COPY . .

RUN pip install mysql-connector-python

CMD ["python", "todo.py"]
