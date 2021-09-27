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
DATABASE=postgres" >> .env.prod
```
Assign <POSTGRES_USER>, <POSTGRES_PASSWORD>, <POSTGRES_USER>, <POSTGRES_PASSWORD> and create file .env.prod.db in app folder
```
echo "POSTGRES_USER=<POSTGRES_USER>
POSTGRES_PASSWORD=<POSTGRES_PASSWORD>
POSTGRES_DB=engineer_django_prod" >> .env.prod.db
```
Build and run docker containers:
```
docker-compose -f docker-compose.prod.yml up -d --build
```
Make migrations:
```
docker-compose -f docker-compose.prod.yml run --rm web_prod python manage.py migrate --noinput
```

## Other commands
### Development
Run containers:
```
docker-compose up -d
```
Check containers:
```
docker-compose ps
```
Read logs:
```
docker-compose logs
```
Run bash:
```
docker run --rm -it --entrypoint bash engineer_web_dev
```
Inspect volumes:
```
docker volume inspect engineer_postgres_data
```
Stop containers:
```
docker-compose down -v
```

### Production
Run containers:
```
docker-compose -f docker-compose.prod.yml up -d
```
Check containers:
```
docker-compose -f docker-compose.prod.yml ps
```
Read logs:
```
docker-compose -f docker-compose.prod.yml logs
```
Run bash:
```
docker run --rm -it --entrypoint bash engineer_web_prod
```
Inspect volumes:
```
docker volume inspect engineer_postgres_data
docker volume inspect engineer_static_volume
docker volume inspect engineer_media_volume
```
Stop containers:
```
docker-compose -f docker-compose.prod.yml down -v
```
## Deinstallation

Remove all stopped containers:
```
docker container prune
```
