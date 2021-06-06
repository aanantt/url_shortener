### URL Shortener

Download and install all the requirements
```
git clone https://github.com/aanantt/url_shortener.git
python -m venv venv
source venv/bin/activate
cd url_shortener/
pip install -r requirements.txt
```

Create Database
```
python manage.py makemigrations
python manage.py migrate
```

Run project on localhost

```
python manage.py runserver
```

## Website
[Click Here](https://shortlinkproject.herokuapp.com/)

