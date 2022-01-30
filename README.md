# Hermes


A web application for planning your bus journies.

## Usage


#### Install the application by cloning this repo:
```
git clone https://github.com/Omgeta/Hermes.git
```


#### Setting environment variables:

Linux/MacOS: 
```
export FLASK_APP=hermes/__init__.py
export FLASK_ENV=development
```

Windows (cmd):
```
set FLASK_APP=hermes\__init__.py
set FLASK_ENV=development
```

Windows (powershell):
```
$env:FLASK_APP = "hermes\__init__.py"
$env:FLASK_ENV = "development"
```



#### Running the application:
```
python -m flask run
```
Note: Make sure you have Werkzeug installed
