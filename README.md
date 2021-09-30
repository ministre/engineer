# Engineer

## About the project

Experimental project.

## Dependencies
### Install Docker Engine
```bash
sudo apt-get update && sudo apt-get upgrade
```
```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
```
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```bash
sudo apt-get update
```
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
```bash
sudo docker run hello-world
```
### Install Docker Compose
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```bash
sudo chmod +x /usr/local/bin/docker-compose
```
```bash
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
```bash
docker-compose --version
```
Add user to docker group:
```bash
sudo usermod -aG docker $USER
```

## Pull the project
```bash
git clone https://github.com/ministre/engineer.git && cd engineer
```

## Installation
Create .env file with assign variables DJANGO_SECRET_KEY, HOSTS, SQL_USER, SQL_PASSWORD:
```bash
echo "DEBUG=0
DJANGO_SECRET_KEY=DJANGO_SECRET_KEY
DJANGO_ALLOWED_HOSTS=HOSTS
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=engineer
SQL_USER=SQL_USER
SQL_PASSWORD=SQL_PASSWORD
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres" >> .env
```
Create .env.prod.db file with assign variables POSTGRES_USER, POSTGRES_PASSWORD:
```bash
echo "POSTGRES_USER=POSTGRES_USER
POSTGRES_PASSWORD=POSTGRES_PASSWORD
POSTGRES_DB=engineer" >> .env.db
```
Build and run docker containers:
```bash
docker-compose up -d --build
```
Create superuser:
```bash
docker-compose run --rm web python manage.py createsuperuser
```

### Checking
Containers status:
```bash
docker-compose ps
```
Logs:
```bash
docker-compose logs
```
Inspect volumes:
```bash
docker volume inspect engineer_postgres_data
```
```bash
docker volume inspect engineer_static
```
Open bash in container:
```bash
docker run --rm -it --entrypoint bash engineer_web
```

## Deinstallation

Stop containers:
```bash
docker-compose down -v
```
Remove images:
```bash
docker image rm engineer_web
```
Remove volumes:
```bash
docker volume rm engineer_postgres_data
```
```bash
docker volume rm engineer_static
```

## References
- https://docs.docker.com/engine/install/ubuntu/
- https://docs.docker.com/compose/install/
