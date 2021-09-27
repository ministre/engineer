# Engineer

## About the project

Experimental project.

## Installation
### Install dependencies
#### Docker Engine
HowTo: https://docs.docker.com/engine/install/ubuntu/
```
sudo apt-get update && sudo apt-get upgrade
```
```
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
```
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
```
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```
sudo apt-get update
```
```
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
```
sudo docker run hello-world
```

#### Docker Compose
HowTo: https://docs.docker.com/compose/install/
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```
sudo chmod +x /usr/local/bin/docker-compose
```
```
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
```
docker-compose --version
```

Add user to docker group:
```
sudo usermod -aG docker $USER
```
#### Install the project
Pull the project:
```
git clone https://github.com/ministre/engineer.git
```
Entering the project folder:
```
cd engineer
```
##### Development
Build and run docker containers:
```
docker-compose -f docker-compose.yml up -d --build
```
Make migrations:
```
docker-compose run --rm web_dev python manage.py migrate --noinput
```
Create superuser:
```
docker-compose run --rm web_dev python manage.py createsuperuser
```
##### Production
Assign <SECRET_KEY>, <HOSTS>, <SQL_USER>, <SQL_PASSWORD> and create file .env.prod in app folder
```
echo "DEBUG=0
SECRET_KEY=<SECRET_KEY>
DJANGO_ALLOWED_HOSTS=<HOSTS>
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=engineer_django_prod
SQL_USER=<SQL_USER>
SQL_PASSWORD=<SQL_PASSWORD>
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres" >> app/.env.prod
```
Assign <POSTGRES_USER>, <POSTGRES_PASSWORD>, <POSTGRES_USER>, <POSTGRES_PASSWORD> and create file .env.prod.db in app folder
```
echo "POSTGRES_USER=<POSTGRES_USER>
POSTGRES_PASSWORD=<POSTGRES_PASSWORD>
POSTGRES_DB=engineer_django_prod
" >> app/.env.prod.db
```
Build and run docker containers:
```
docker-compose -f docker-compose.prod.yml up -d --build
```

## Other commands
Check containers:
```
docker-compose ps
```

### Development
### Production
To run containers:
```
docker-compose -f docker-compose.prod.yml up -d
```
To stop containers:
```
docker-compose -f docker-compose.prod.yml down -v
```
To read logs:
```
docker-compose logs -f
```
To run bash in container:
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
