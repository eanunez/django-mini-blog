#Django Mini-blog Backend

This is a demo of django rest API backend using a mini-blog project.

## Installation
1) Clone the repository.
2) Create a virtual environment and activate.
3) `pip install -r requirements.txt`
4) CD to the parent directory: `$ cd blog`
5) Create migrations: 
   ```
   $ python manage.py makemigrations
   $ python manage.py migrate
   ``` 
6) Load the data by running: `python manage.py loaddata data.json`
4) Run the server: `python manage.py runserver`