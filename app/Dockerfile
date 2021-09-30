###########
# BUILDER #
###########

# pull official base image
FROM python:3.8 as builder

# set work directory
WORKDIR /opt/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./engineer_django/requirements.txt .

# install dependencies
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /opt/app/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.8

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
#RUN apt-get update && \
#    apt-get -y install netcat gettext && \
#    apt-get clean

COPY --from=builder /opt/app/wheels /wheels
RUN pip install --no-cache /wheels/*

# copy project
RUN mkdir engineer_django
COPY . .
RUN mkdir engineer_django/static

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# set work directory
WORKDIR $APP_HOME/engineer_django

# django collect statics, compile localization messages, make migrations
RUN python manage.py collectstatic --no-input --clear
RUN python manage.py compilemessages --no-input
RUN python manage.py makemigrations --no-input

# run entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
