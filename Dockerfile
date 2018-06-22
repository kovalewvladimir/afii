FROM python:3

WORKDIR /afii

add https://raw.githubusercontent.com/kovalewvladimir/afii/deploy/requirements.txt /tmp/requirements.txt

RUN apt-get update && apt-get -y install libldap2-dev libsasl2-dev libssl-dev
RUN pip install -r /tmp/requirements.txt

EXPOSE 8000

CMD ["python", "/afii/afii/manage.py", "runserver", "0.0.0.0:8000"]