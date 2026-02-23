FROM python:3.14-slim

# Copy application files
WORKDIR /app
COPY config.py .
COPY flairtimercomment.py .

RUN mkdir -p /app/config

# Install dependencies
RUN pip install --no-cache-dir praw 

ENV PYTHONUNBUFFERED=1

# Run the script
CMD ["python", "flairtimercomment.py"]


