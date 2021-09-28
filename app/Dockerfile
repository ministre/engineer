# pull official base image
FROM python:3.8

# set work directory
WORKDIR /opt/app/engineer_django

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# install dependencies
RUN apt-get update && \
    apt-get -y install netcat gettext && \
    apt-get clean

RUN pip install --upgrade pip
RUN pip install -r engineer_django/requirements.txt

# run entrypoint.sh
ENTRYPOINT ["/opt/app/entrypoint.sh"]
