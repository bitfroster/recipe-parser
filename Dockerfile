FROM python:3.12

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY models /app/
COPY config.py /app/
COPY lib /app/
COPY main.py /app/
COPY tests /app/

CMD [ "python", "/app/main.py" ]