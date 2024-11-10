FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    jq \
    firefox-esr \
    && rm -rf /var/lib/apt/lists/*

RUN GECKODRIVER_VERSION=0.32.0 \
    && wget -N https://github.com/mozilla/geckodriver/releases/download/v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz \
    && tar -xvzf geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && rm geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz

ENV DISPLAY=:99
ENV FIREFOX_BIN=/usr/bin/firefox-esr
ENV GECKODRIVER=/usr/local/bin/geckodriver

WORKDIR /worker

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /worker

CMD ["celery", "-A", "worker_scrape.tasks", "worker", "--loglevel=info"]
