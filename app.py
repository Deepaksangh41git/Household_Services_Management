from flask import Flask
from back_end.config import LocalDevelopmentConfig
from back_end.models import db,User,Role
from flask_security import Security,SQLAlchemyUserDatastore
from flask import render_template_string,render_template
from flask_security import auth_required, current_user, roles_required
from back_end.resources import api

def Create_App():
    app=Flask(__name__, template_folder='front_end', static_folder='front_end', static_url_path='/static')
    app.config.from_object(LocalDevelopmentConfig)

    db.init_app(app)
    #flash securirty
    x_datastore=SQLAlchemyUserDatastore(db,User,Role)

    api.init_app(app)

    app.security=Security(app, datastore=x_datastore,register_blueprint=False)
    app.app_context().push()
    return app

app=Create_App()
import back_end.routes
import back_end.create_initial_data

if (__name__ =='__main__'):
    app.run(debug=True)
