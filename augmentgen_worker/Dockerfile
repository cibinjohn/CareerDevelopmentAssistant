FROM python:3.8-slim

# layer caching for faster builds
COPY requirements.txt /
RUN pip install -r /requirements.txt

#COPY app.py /app.py
ADD . /augmentgen_worker
COPY src /augmentgen_worker/src

WORKDIR /augmentgen_worker/src

ENTRYPOINT celery -A tasks worker --concurrency=1 --loglevel=info
#-Q celery_worker
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']