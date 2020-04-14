# aa-api/app.py

from flask import Flask
from database.db import initialize_db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/aa-motors'
}

initialize_db(app)


app.run()
