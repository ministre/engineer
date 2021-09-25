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
RUN pip install --upgrade pip
RUN pip install -r engineer_django/requirements.txt
