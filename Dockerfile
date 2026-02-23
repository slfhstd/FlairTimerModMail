FROM python:3.14-slim

# Copy application files
WORKDIR /app
COPY config.py .
COPY flairtimermodmail.py .

RUN mkdir -p /app/config

# Install dependencies
RUN pip install --no-cache-dir praw 

ENV PYTHONUNBUFFERED=1

# Run the script
CMD ["python", "flairtimermodmail.py"]


