# instagram-backend

Instagram REST API with basic features real Instagram has.

## Quick Start

1. Clone Git repository

```
git clone https://github.com/konradgalczynski07/doitforalex-instagram-backend-start
```

2. Create .env file by copying .env_example

```
cp .env_example .env 
```

3. Set required env variables in .env file

```
SECRET_KEY=test
DEBUG=True
ALLOWED_HOSTS=*
CORS_ORIGIN_WHITELIST=http://localhost:3000
```
4. Bulid project with docker-compose and make sure everything works
```
docker-compose up --build
```

If all above steps are completed successfully you are ready to develop using Docker. 

**However to better experience we advice you** to develop locally using dockerized db and frontend running and start Django on your local machine with virtualenv. To do that: 

5. Change *POSTGRES_HOST* and *DATABASE_URL* env vars to use your localhost. Simply uncommment them out like so:

```
DATABASE_URL=postgres://postgres:postgres@localhost:5432/instagram
# DATABASE_URL=postgres://postgres:postgres@instagram-postgres:5432/instagram
POSTGRES_HOST=localhost
# POSTGRES_HOST=instagram-postgres
```

8. Export .env file or add it to your workspace config

```
set -o allexport; source .env; set +o allexport;
```

7. Now create and activate your local venv

```
python3 -m venv venv
source venv/bin/activate
```

7. Install dependencies

```
pip install -r requirements.txt
```

8. Run db and frontend with docker-compose

```
docker-compose up -d postgres frontend
```

9. Run local server

```
python instagram-backend/manage.py runserver
```

10. Open you localhost:3000 and localhost:8000 in browser and check out it works. 

## Makefile

For your convenience we created *Makefile* in which we place all commands mentioned above. 

They enable you to type aliases in your command line. 

eg. 

```
make db 
=
docker-compose up -d postgres 
```

```
make frontend
=
docker-compose up -d frontend
```

To check out full list and familiarize yourself with *Makefile*


## Happy coding !