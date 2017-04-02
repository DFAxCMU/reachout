# reachout

## Setup

#### Windows
```
virtualenv venv
venv\scripts\activate
pip install -r requirements.txt
python manage.py migrate --run-syncdb
```

#### Mac
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate --run-syncdb
```

## Running

#### Windows

#### Mac
```
source venv/bin/activate
python manage.py runserver
```

#### Windows
```
venv\scripts\activate
python manage.py runserver
```
