# Simple Flask  app for TechLabs' workshop 

# How to run

1. Install Flask and pandas using `pip install <package name>`
2. Export Flask app name variable. Depending on yur system the command can look like: `export FLASK_APP=flask_app` (Bash) or `set FLASK_APP=flask_app` (CMD) or `$env:FLASK_APP = "flask_app"` (Powershell)
3. Run with `flask run`

Documentation: https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application

# How to use

Get all data: http://myfirstflaskapp.pythonanywhere.com/api/wines/all

Get a wine by id: http://myfirstflaskapp.pythonanywhere.com/api/wines?id=1

Filter wines by quality: http://myfirstflaskapp.pythonanywhere.com/api/wines/filter?quality=8

# Resources
Dataset http://archive.ics.uci.edu/ml/datasets/Wine+Quality

Deploy on https://www.pythonanywhere.com/

Tutorials:

https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application

https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask 

https://blog.pythonanywhere.com/121/
