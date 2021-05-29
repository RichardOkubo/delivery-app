:: Alternative to "make init_db" (Windows prompt)
set FLASK_APP=delivery/app.py
flask create-db
flask db upgrade