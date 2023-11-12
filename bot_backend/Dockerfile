FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y bash jq apt-utils cron curl python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install instaloader Flask flask_cors ip2geotools

RUN apt-get update && \
    apt-get install -y awscli && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN aws configure set aws_access_key_id ""

RUN aws configure set aws_secret_access_key ""

RUN aws configure set default.region us-east-1

RUN aws s3 sync s3://wednesdayos/accounts/ accounts --delete

RUN (echo "30 * * * * /app/backup.sh" | crontab -)

EXPOSE 5000

ENV FLASK_APP app.py

CMD ["flask", "run", "--host=0.0.0.0"]