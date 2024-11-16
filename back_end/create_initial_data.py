from flask_security import SQLAlchemyUserDatastore
from flask_security.utils import hash_password
from back_end.models import db
from app import app

with app.app_context():
    db.create_all()
    user_datastore: SQLAlchemyUserDatastore = app.security.datastore

    #creating roles
    user_datastore.find_or_create_role(name='admin',description="admin" )
    user_datastore.find_or_create_role(name="Customer",description="Customer" )
    user_datastore.find_or_create_role(name="Porfessional",description="Service Porfessional" )
    
    #creating data
    if not user_datastore.find_user(email="Admin@iitmmad2project.com"):
        user_datastore.create_user(email="Admin@iitmmad2project.com",password=hash_password("Admin"),active=True,roles=["admin"])
    if not user_datastore.find_user(email="Customer@iitmmad2project.com"):
        user_datastore.create_user(email="Customer@iitmmad2project.com",password=hash_password("Customer"),active=True,roles=["Customer"])
    if not user_datastore.find_user(email="Porfessional@iitmmad2project.com"):
        user_datastore.create_user(email="Porfessional@iitmmad2project.com",password=hash_password("Porfessional"),active=True,roles=["Porfessional"])
    db.session.commit()