# instagram-backend

Instagram REST API with basic features real Instagram has.

## Quick Start

1. Download or clone git repository and open project in your code editor

```
git clone https://github.com/konradgalczynski07/doitforalex-instagram-backend-start
```

2. Then open terminal in code editor to create .env file by copying .env_example

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

4. Export .env vars

```
set -o allexport; source .env; set +o allexport;
```

5. Now create and activate your local venv

```
python3 -m venv venv
source venv/bin/activate
```

6. Install dependencies

```
pip install -r requirements.txt
```

7. Run db and frontend provided with docker-compose

```
docker-compose up
```

8. Run local server

```
python instagram-backend/manage.py runserver
```

9. Open localhost:3000 and localhost:8000 in your browser and check out whether frontend and backend works.

## Makefile

For your convenience we created *Makefile* in which we place all commands mentioned above. 

They enable you to type aliases in your command line. 

eg. 

```
make db 
=
docker-compose up postgres 
```

```
make frontend
=
docker-compose up frontend
```

To check out full list and familiarize yourself with *Makefile*


## Happy coding !