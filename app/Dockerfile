# pull official base image
FROM python:3.8
# set work directory
WORKDIR /opt
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# download project
RUN git clone https://github.com/ministre/engineer.git
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r engineer/app/engineer_django/requirements.txt
