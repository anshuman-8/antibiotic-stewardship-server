# ANTIBIOTIC STEWARDSHIP SERVER
![STEWARDSHIP-server](https://github.com/anshuman-8/antibiotic-stewardship-server/assets/90995338/4559b2c3-6623-40e5-9cf0-c71df04a845f)

- Clone and setup the repository
```bash
git clone https://github.com/anshuman-8/antibiotic-stewardship-server.git # clone the repo
cd antibiotic-stewardship-server
# make a python virtual environment
sudo pip3 install virtualenv 
virtualenv venv 
```
- Setup Database (Steps given down at **Setting up Database**)

- Activate the environment
```bash
source venv/bin/activate
```
#### create .env file and set variables.

```env
DEVELOPMENT=True
SECRET_KEY="<SECRET_KEY>"
DB_HOST=localhost
DB_PORT=5432
DB_NAME=<DATABASE_NAME>
DB_USER_NAME=<DATABASE_USER_NAME>
DB_PASSWORD=<DATABASE_PASSWORD>

```
> **_NOTE:_** Replace <<v>values> with actual values
  

```bash
pip install -r requirements.txt
```
```bash
python3 manage.py migrate
```
```bash
python3 manage.py runserver
```

### Setting up Database

1. Install PostgreSQL (For Ubuntu users [Download Guide](https://cloudinfrastructureservices.co.uk/how-to-install-postgresql-on-ubuntu-22-04-server/))

2. login to Postgres by 
    ```bash
    sudo su — postgres
    psql
    ```

3. Create a user with a password and DB and grant permission on DB from the user
    ```sql
    create user <username>;
    create database stewardship;
    alter role <username> with password 'stewardship@123';
    grant all privileges on database stewardship to <username>;
    alter database stewardship owner to <username>;
    ```
> **_NOTE:_** All above values given are dummy!, replace `<username>` with your name

4. In [.env](./.env) update DATABASES config

