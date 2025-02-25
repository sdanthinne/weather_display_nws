from python:3.12

workdir /srv

copy ./requirements.txt requirements.txt

run pip3 install -r requirements.txt

copy ./weather-gov-api-client weather-gov-api-client

workdir /srv/weather-gov-api-client

run pip3 install .

workdir /srv

copy ./app /srv/app

workdir /srv/app

cmd ["fastapi", "run", "main.py", "--port", "80", "--proxy-headers"]
