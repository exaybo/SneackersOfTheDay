FROM python
#prepare chrominium and chrome driver
#https://www.blazemeter.com/blog/selenium-docker
RUN wget -q "https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip
RUN apt-get update && apt-get install -yq chromium


RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/

#install selenium and so on
RUN pip install -r requirements.txt

CMD ["python", "SneackersCrowler.py"]