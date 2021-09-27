# pull official base image
FROM python:3.8

# set work directory
WORKDIR /opt/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# install dependencies
RUN apt-get update && \
    apt-get -y install apt-utils netcat && \
    apt-get clean

# create virtual environment
RUN python3 -m venv env
RUN source /opt/app/env

# set work directory
WORKDIR /opt/app/engineer_django

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# run entrypoint.sh
ENTRYPOINT ["/opt/app/entrypoint.sh"]
