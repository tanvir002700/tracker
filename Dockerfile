MAINTAINER tanvir002700@gmail.com

FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000

CMD cd office_tracker && python manage.py runserver --settings=office_tracker.settings.docker 0.0.0.0:8000
