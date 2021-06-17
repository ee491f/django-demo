# Django Demo
A demonstration of the Django material for [EE491F](https://ee491f.github.io/course-material/#django "EE491F Course Webpage").  
Accompanying Videos:
* Set Up Environment: [https://youtu.be/pdP-pBIziIo](https://youtu.be/pdP-pBIziIo "Getting Started with Django: Set Up Environment Video")
* Create App: [https://youtu.be/FMzXx1TUs58](https://youtu.be/FMzXx1TUs58 "Getting Started with Django: Create App Video")
* Start App: [https://youtu.be/KOrnmwVeRS4](https://youtu.be/KOrnmwVeRS4 "Getting Started with Django: Start App Video")
* Update App: [https://youtu.be/OxJOfsuvNwU](https://youtu.be/OxJOfsuvNwU "Getting Started with Django: Update App Video")

Outline
-------
1. Set Up Python Environment
1. Create New Django App
1. Start App
1. Update App

# Heroku Demo
A demonstration of the Django material for [EE491F](https://ee491f.github.io/course-material/#heroku "EE491F Course Webpage").  
Accompanying Videos:
* Set Up Heroku App: [https://youtu.be/GkKNg25Piho](https://youtu.be/GkKNg25Piho "Getting Started with Heroku: Set Up Heroku App Video")
* Update Django App: [https://youtu.be/cZlURocbJzQ](https://youtu.be/cZlURocbJzQ "Getting Started with Django: Update Django App Video")
* Add PostgreSQL Database: [https://youtu.be/99Z9f5YBN2s](https://youtu.be/99Z9f5YBN2s "Getting Started with Django: Add PostgreSQL Database Video")

Outline
-------
1. Set Up Heroku App
    1. Login to Heroku: `heroku login`
    1. Login to Heroku's Container Registry: `heroku container:login`
    1. Create Heroku App: `heroku create heroku-demo-ee491f`
    1. Build and Push Image to Heroku's Registry: `heroku container:push web`
    1. Have Heroku Use Pushed Image: `heroku container:release web`
    1. View Heroku App: `heroku open`
    1. Follow Heroku logs: `heroku logs --tail`
    1. Use Heroku's Web Console
    1. Use Heroku's CLI Console: `heroku run bash`
1. Update Django App
    1. Update Container Startup Command:
        ```
        ### Dockerfile ###
        CMD script/start_app.sh
        ```
    1. Copy Source Code into Container:
        ```
        ### Dockerfile ###
        COPY . /usr/src/app/
        ```
    1. Update Port
        ```
        ### scripts/start_app.sh
        ./manage.py runserver 0.0.0.0:"$PORT"
        ```
        ```
        ### app.env ###
        PORT=8000
        ```
    1. Use Heroku's Django Library: `django-heroku`
        * https://devcenter.heroku.com/articles/django-app-configuration
          ```
          ### requirements.txt ###
          django-heroku ~= x.y.z
          ```
          ```
          ### mysite/settings.py ###
          import django_heroku
          ...
          django_heroku.settings(locals())
          ```
1. Add PostgreSQL Database
    1. Local Development
        * Update `docker-compose.yml` to include `database` service
          ```
          ### docker-compose.yml ###
          services:
            ...
            database:
              image: postgres:11.12
              env_file:
                - database.env
              volumes:
                - database-data:/var/lib/postgresql/data/

          volumes:
            database-data: 
          ```
        * https://docs.djangoproject.com/en/3.2/ref/settings/
          ```
          ### mysite/settings.py ###
          DATABASES = {
              'default': {
                  'ENGINE': 'django.db.backends.postgresql',
                  'NAME': os.environ['POSTGRES_DB'],
                  'USER': os.environ['POSTGRES_USER'],
                  'PASSWORD': os.environ['POSTGRES_PASSWORD'],
                  'HOST': os.environ['DATABASE_HOST'],
                  'PORT': os.environ['DATABASE_PORT'],
              }
          }
          ```
    1. Remote Production
        1. Configure environment variables
        1. Add `heroku-postgresql` addon
