# Mezzanine on Heroku

A clean install of [Mezzanine CMS](http://mezzanine.jupo.org/) with the [Cartridge](http://cartridge.jupo.org/index.html) e-commerce extension, with an [API](https://github.com/jackvz/mezzanine-cartridge-api) for connecting [iOS and Android apps](https://github.com/jackvz/flutter-app-with-mezzanine) for example, that integrates with [Stripe](https://stripe.com/) for payment processing, and that is configured to deploy to [Heroku](https://www.heroku.com/) and to use [Amazon S3](https://aws.amazon.com/s3/) for media storage.

Do an automated deploy to Heroku and select one of the [free themes for Mezzanine](https://github.com/thecodinghouse/mezzanine-themes), Flat, Moderna, Nova or Solid:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

1. [Build](#build)
2. [Deploy](#deploy)
3. [Theme](#theme)

<a name="build"></a>
## Build

### Install [Python](https://www.python.org/) and [PostgreSQL](https://www.postgresql.org/)

### Start a Python [virtual environment](https://virtualenv.pypa.io/en/latest/)

Clone the repository and run:

```bash
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

### Configure the system

In onlineshop/settings.py and onlineshop/heroku_settings.py, set values for the following:
- SECRET_KEY - [Django secret key generator](https://djskgen.herokuapp.com/)
- NEVERCACHE_KEY
- SHOP_CURRENCY_LOCALE - Defaults to US. For example 'en_US.UTF-8', 'en_GB.UTF-8' or 'af_ZA.UTF-8'
- STRIPE_API_KEY - [Stripe dashboard](https://dashboard.stripe.com/)
- AWS_ACCESS_KEY_ID - [AWS security credentials](https://console.aws.amazon.com/iam/home#/security_credentials)
- AWS_SECRET_ACCESS_KEY
- AWS_STORAGE_BUCKET_NAME - [AWS storage console](https://s3.console.aws.amazon.com/s3/home)
- EMAIL_HOST
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD
- DEFAULT_FROM_EMAIL

### Install a clean database

Create a local PostgreSQL database called `onlineshop`

Run all migrations:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

If the theme is not used and all default settings are restored, no migrations are necessary so just create the database:

```bash
python3 manage.py createdb --noinput --nodata
```

### Run the development web server

Collect the static files:

```bash
python3 manage.py collectstatic
```

Run a [Django](https://www.djangoproject.com/) development server:

```bash
python3 manage.py runserver
```

Browse to [http://localhost:8000/](http://localhost:8000/)

Run a [Gunicorn](https://gunicorn.org/) web server similar to Heroku:

```bash
heroku local -f local-heroku.procfile
```

Browse to [http://localhost:5000/](http://localhost:5000/)

For managing content with Mezzanine, browse to [http://localhost:8000/admin](http://localhost:8000/admin)

The default super user is 'admin' and the password is 'default'. You should change this.

To clear the static file cache:

```bash
python3 manage.py clear_cache
```

### Work with the API

Add an API key via the admin and note the token and secret key: [http://localhost:8000/admin/rest_framework_api_key/apikey/add/](http://localhost:8000/admin/rest_framework_api_key/apikey/add/)

Browse to the API documentation at [http://localhost:8000/api/docs](http://localhost:8000/api/docs), click the Authorize button and enter the token and secret key, and then try out any of the API calls.

### Deactivate the virtual environment

If you need to recreate the virtual environment, perhaps to clear any changes you made directly to any of the installed Python packages, deactivate the virtual environment first:

```bash
deactivate
```

<a name="deploy"></a>
## Deploy

Download the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

Login:

```bash
heroku login
```

Create an app:

```bash
heroku create
```

Note the Heroku app name, and add the Heroku Git repository as a remote to this Git repository:

```bash
heroku git:remote -a [heroku-app-name]
```

Configure [New Relic](https://newrelic.com/):

```bash
heroku addons:create newrelic:wayne
heroku config:set NEW_RELIC_APP_NAME=[heroku-app-name]
```

Deploy the code:

```bash
git push heroku master
```

If the Amazon S3 media file storage configuration is removed, then the Mezzanine Media Library in staticfiles/media is included in the Git repo, and can be included in the deploy.

Create a PostgreSQL database for Mezzanine on Heroku

```bash
heroku run python manage.py createdb --noinput --nodata --settings=onlineshop.heroku_settings
```

### Production

View production site:

```bash
heroku open
```

Access the production PostgreSQL database:

```bash
heroku pg:psql [heroku-database-name] --app [heroku-app-name]
```

Put Heroku app in maintenance mode to display a user friendly offline page:

```bash
heroku maintenance:on
```

Run a Mezzanine/Django Python shell on Heroku, for example, create a super user:

```bash
heroku run python manage.py shell --settings=onlineshop.heroku_settings`
```

```python
from django.contrib.auth.models import User
user=User.objects.create_user('foo', password='bar')
user.is_superuser=True
user.is_staff=True
user.save()
```

### Content publication workflow

Create a local Mezzanine PostgreSQL database backup:

```bash
pgpassword=[db-password] pg_dump -Fc --no-acl --no-owner -h localhost -U [postgres-user] [db-name] > mydb.dump
```

Generate a signed URL for a database backup that was uploaded to [Amazon S3 storage](https://console.aws.amazon.com/s3/):

```bash
aws s3 presign s3://[s3-bucket-name]/mydb.dump
```

Restore a Mezzanine PostgreSQL database backup to Heroku from Amazon S3, using a signed URL:

```bash
heroku pg:backups:restore [aws-s3-signed-url] [heroku-db-name] --confirm [heroku-appname]
```

If only database structural changes were made and no actual data changed, then Heroku could be updated with Django migrations:

```bash
heroku run "python manage.py makemigrations [django-appname] --settings=onlineshop.heroku_settings && python manage.py migrate [django-appname] --settings=onlineshop.heroku_settings"
```

<a name="theme"></a>
## Theme

For an excellent article on creating a theme, see this [Bit of Pixels article](http://bitofpixels.com/blog/mezzatheming-creating-mezzanine-themes-part-1-basehtml/).
