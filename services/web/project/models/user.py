from werkzeug.security import generate_password_hash, check_password_hash
#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from project.shared.database import db


def model_exists(model_class):
    #engine = db.get_engine(bind=model_class.__bind_key__)
    #return model_class.metadata.tables[model_class.__tablename__].exists(engine)
    print('testing model exists')

class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {'mysql_charset': 'utf8', 'mysql_engine': 'InnoDB'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, username, password, email ):
        self.username = username
        self.password = password
        self.email = email


    def set_password(self, password):
        self.password = generate_password_hash(password)
        print("Password is ", self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'active': self.active,
            'admin': self.admin
        }
