from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin,UserMixin
from datetime import datetime
from flask_security.models import fsqla_v3 as fsq

db=SQLAlchemy()

fsq.FsModels.set_db_info(db)

class Role(db.Model,RoleMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True,nullable=False)
    description=db.Column(db.String,nullable=False)

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String,nullable=False)
    #flask sec. specfic
    fs_uniquifier=db.Column(db.String,unique=True,nullable=False)
    active=db.Column(db.Boolean,default=True)
    roles=db.Relationship('Role',secondary='user_roles')

class UserRoles(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'))

#Admin
class Admin(User):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

#Customer
class Customer(User):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    # Relationship to ServiceRequest
    service_requests = db.relationship('ServiceRequest', backref='customer', lazy=True)

#ServiceProfessional
class ServiceProfessional(User):
    __tablename__ = 'service_professional'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    profession = db.Column(db.String(100), nullable=False)
    verified = db.Column(db.Boolean, default=False)  # Approved by admin
    bio = db.Column(db.Text)
    # Relationship to ServiceRequest
    service_requests = db.relationship('ServiceRequest', backref='professional', lazy=True)

# Service Model for Service Management
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    base_price = db.Column(db.Float, nullable=False)
    time_required = db.Column(db.Integer)  # in minutes

# Service Request Model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey('service_professional.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    date_of_request = db.Column(db.DateTime)
    completion_status = db.Column(db.String(20), default='Pending')  # e.g., Pending, Accepted, Rejected, Completed
    remarks = db.Column(db.Text)
    # Relationships
    service = db.relationship('Service', backref=db.backref('requests', lazy=True))