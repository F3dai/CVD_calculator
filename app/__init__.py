from flask import Flask


app = Flask(__name__,template_folder='templates')
from app import views
from app.modules import risk, db




def create_app():
    from flask import Flask
    app = Flask(__name__,template_folder='templates')

    from app import views
    from app.modules import risk, db
