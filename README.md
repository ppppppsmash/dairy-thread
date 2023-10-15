# Dairy-thread

## create python dev env
conda create -n django-app python=3.9

conda info -e

conda activate django-app

conda install django

conda list

django-admin startproject dairy_thread
cd dairy_thread

python manage.py startapp accounts

## make a migration file
python manage.py makemigrations accounts

## migrate the db table with the migration file
python manage.py migrate


### sqlite3
sqlite3 db.sqlite3

.table

select * from {table};

.schema

.quit
