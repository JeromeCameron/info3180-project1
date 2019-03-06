from . import db

class UserProfile(db.Model):
    
    __tablename__ = 'user_profiles'

    ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(255))
    biography = db.Column(db.String(255))
    created_on = db.Column(db.String(10))
    
    
    def __init__(self, first_name, last_name, gender, email, location, biography, created_on):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.created_on = created_on
        