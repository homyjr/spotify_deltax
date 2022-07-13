
# Spotify

Basic web app with CRUD operations using django

# Watch the demo

* recorded video of functioning of the web application

    https://screenrec.com/share/oygz2SW65Y

# To run the project using docker image

    docker run -p 8000:8000 homydocker/spotify_deltax:v1

 * open the web app in browser

    http://127.0.0.1:8000/   
    
# Manual installation

* download the project in a folder of your choice

* change the directory

```bash
cd spotify_deltax/spotify
```

* install the requirements

```bash
pip install -r requirements.txt
```

* run the application

```bash
python manage.py runserver 
```

* open the web app in browser

    http://127.0.0.1:8000/


#  Extras

For database  models check out "/app/models.py"

* For generated sql queries check out 

``` bash
python manage.py sqlmigrate app 0001

```
* changes done after creating tables in the database

```bash
python manage.py sqlmigrate app 0002
python manage.py sqlmigrate app 0003
```
