FROM python

RUN pip install selenium
RUN wget -q "https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip
RUN apt-get update && apt-get install -yq chromium


RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

CMD ["python", "SneackersCrowler.py"]