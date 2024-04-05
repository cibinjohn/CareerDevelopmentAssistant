FROM python:3.10-slim
RUN mkdir /app
COPY requirements.txt /app/
RUN cd /app
RUN ls
RUN pip install --upgrade pip
RUN pip3 install -r /app/requirements.txt

COPY src /app/src


# Set environment variables
ENV APP_PORT=7000
ENV APP_HOST=0.0.0.0
ENV LOGFILE="/app/src/log/log.txt"
ENV CHROMA_PATH="/app/src/chroma"
ENV MONGODB_PORT=27017
ENV MONGODB_HOST="mongodb"
ENV MONGODB_NAME="careerdevelopment_db"

EXPOSE 6999

WORKDIR /app/src

# CMD ["python", "wsgi.py"]
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:6999", "wsgi:app"]