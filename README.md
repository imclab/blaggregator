This is a blog post aggregator for the Hacker School community. 

**Want to contribute? Check out [Contribute.md](CONTRIBUTE.md).**

### Installation: 

- Set up your virtual environment

- Install dependencies:

`pip install -r requirements.txt`

- Static assets are hosted on S3. Make a new S3 bucket and grab your security credentials. Put your keys in your environmental variables: 

```
export AWS_ACCESS_KEY_ID=''
export AWS_SECRET_ACCESS_KEY=''
```

And in `settings.py` update `AWS_STORAGE_BUCKET_NAME` to be the bucket name you picked.

Then run `collectstatic` to grab all your static assets and send them to S3 where your app can access them. You'll need to run this again each time you change your static assets. 

`python manage.py collectstatic`

- Set up your database. Open a Postgres shell: 

`python manage.py dbshell`

and create your database: 

`CREATE DATABASE blaggregator_dev;`

The semicolon is critical. Then go back to bash and populate the database from the app's models. IMPORTANT: when you are creating your admin account, *don't* use the same email address as your Hacker School account or you won't be able to create a user account for yourself. Do username+root@example.com or something.

`python manage.py syncdb`

If you get this error: 

```
OperationalError: could not connect to server: No such file or directory
Is the server running locally and accepting
connections on Unix domain socket "/var/pgsql_socket/.s.PGSQL.5432"?
```

Then open `settings.py` and under `HOST:` add `/tmp`. 

- Optional but helpful: turn on debugging in your environment:

`export DJANGO_DEBUG=True`

- Then run a local server:

`python manage.py runserver`

You can administer your app through the [handy-dandy admin interface](http://localhost:8000/admin). You can be logged in as the admin or as your user account, but not both at the same time.