FROM python:3.8-slim

# layer caching for faster builds
COPY requirements.txt /
RUN pip install -r /requirements.txt


#COPY app.py /app.py
ADD . /flask_app
COPY src /flask_app/src
WORKDIR /flask_app/src

ENV FLASK_ENV=development

EXPOSE 7006

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:7006", "-t", "6000", "app:app"]
# CMD flask run --host=0.0.0.0

#CMD gunicorn --workers $WORKERS \
#  --threads $THREADS \
#  --bind 0.0.0.0:$PORT_APP \
#  --log-level DEBUG \
#  app:app