# Callback bot
## create .env
```bash
cp env.example .env
nano .env
```
## start (docker)
```bash
docker compose up
```
## start
vk общается с сервером только по 80 порту
```bash
poetry env activate
poetry install --no-root
cd app
gunicorn 0.0.0.0:80 bot:app
```
