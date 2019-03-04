from . import db
# from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(255))
    biography = db.Column(db.String(255))
    #photo = db.Column(db.bytea())
    #date_joind = db.Column(db.date())
    
    
    def __init__(self, first_name, last_name, gender, email, location, biography, photo, date_joind):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo
        self.date_joind = date_joind