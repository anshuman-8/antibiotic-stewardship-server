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
### create .env file and set variable

```env
DEVELOPMENT=True
SECRET_KEY="<SECRET_KEY>"
DB_HOST=localhost
DB_PORT=5432
DB_NAME=stewardship
DB_USER_NAME=<DATABASE_NAME>
DB_PASSWORD=<DATABASE_PASSWORD>

```
Note: Replace <<v>values> with actual values

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
Note: All above values given are dummy!

4. In [.env](./.env) update DATABASES confg

