# Engineer

## About the project

Experimental project.

## Installation
### Development
### Production
Build and run docker containers:
```
docker-compose -f docker-compose.prod.yml up -d --build
```
Make migrations:
```
docker-compose -f docker-compose.prod.yml exec web python engineer_django/manage.py migrate --noinput
```

## Useful commands
### Development
### Production
To run docker containers:
```
docker-compose -f docker-compose.prod.yml up -d
```
To stop docker containers:
```
docker-compose -f docker-compose.prod.yml down -v
```
To read logs:
```
docker-compose logs -f
```
To run bash in docker container:
```
docker run --rm -it --entrypoint bash engineer_web
docker run --rm -it --entrypoint bash engineer_nginx
```
To inspect volumes:
```
docker volume inspect engineer_postgres_data
docker volume inspect engineer_static_volume
docker volume inspect engineer_media_volume
```
