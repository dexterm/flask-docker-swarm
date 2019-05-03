from flask.cli import FlaskGroup
from project.app import create_app
from project.models.user import User
from project.models.oauth2 import OAuth2Client, OAuth2AuthorizationCode, OAuth2Token
#from project.models import *

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    #if model_exists('Users'):
    #  print("Model User exists");
    #db.init_app(app)
    from project.shared.database import db
    #create users first
    User.__table__.create(db.session.bind, checkfirst=True)
    OAuth2Client.__table__.create(db.session.bind, checkfirst=True)
    OAuth2AuthorizationCode.__table__.create(db.session.bind, checkfirst=True)
    OAuth2Token.__table__.create(db.session.bind, checkfirst=True)

    #db.drop_all()
    #db.create_all()
    db.session.commit()
    #with app.app_context():
    #    db.drop_all()
    #    db.create_all()
    #    db.session.commit()


@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    from project.shared.database import db

    u = User(username="dexter", password="dexter", email="djcm95@gmail.com")
    u.set_password("dexter")

    db.session.add(u)
    db.session.commit()
    #below our user model, we will create our hashing functions

if __name__ == '__main__':
    cli()
