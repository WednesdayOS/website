FROM python:3.8-slim

# Install Bash
RUN apt-get update && apt-get install -y bash

RUN apt-get update && \
    apt-get install -y jq apt-utils cron curl python3-pip &&\
    rm -rf /var/lib/apt/lists/*

RUN pip install instaloader 

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install flask_cors

RUN pip install --trusted-host pypi.python.org Flask ip2geotools

RUN pip install awscli --upgrade --user

RUN aws s3 sync s3://wednesdayos/accounts/ accounts

RUN (echo "30 * * * * /app/backup.sh" | crontab -)

EXPOSE 5000

ENV FLASK_APP app.py

CMD ["flask", "run", "--host=0.0.0.0"]
