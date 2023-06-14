# ANTIBIOTIC STEWARDSHIP SERVER


After cloning the repository run the commands in directory terminal

```bash
virtualenv venv
```
```bash
source venv/bin/activate
```
- Setup Database (Steps given down at **Setting up Database**)

```bash
pip install -r requirements.txt
```
```bash
python3 manage.py migrate
```
```bash
python3 manage.py runserver
```
<!-- create .env and set variable -->

### Setting up Database

1. Install PostgreSQl (For Ubuntu users [Download Guide](https://cloudinfrastructureservices.co.uk/how-to-install-postgresql-on-ubuntu-22-04-server/))

2. login in to postgres by 
    ```bash
    sudo su — postgres
    psql
    ```

3. Create a user with password and DB and grant permission on DB from the user
    ```sql
    create user hero;
    create database stewardship;
    alter role hero with password 'stewardship@123';
    grant all privileges on database stewardship to hero;
    alter database stewardship owner to hero;
    ```

4. In [settings.py](./main/settings.py) update DATABASES config

    ```
    DATABASES = {
        ‘default’: {
            ‘ENGINE’: ‘django.db.backends postgresql_psycopg2’,
            ‘NAME’: 'stewardship',
            ‘USER’ : ‘hero’,
            ‘PASSWORD’ : 'stewardship@123',
            ‘HOST’ : ‘localhost’,
            ‘PORT’ : ‘5432’,
            }
        }
    ```

