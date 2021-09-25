# pull official base image
FROM python:3.8

# set work directory
WORKDIR /opt/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY ./engineer_django/ ./engineer_django/

# install dependencies
RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
RUN pip install -r engineer_django/requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# run entrypoint.sh
ENTRYPOINT ["/opt/app/entrypoint.sh"]
