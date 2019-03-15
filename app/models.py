from . import db

class UserProfile(db.Model):
    
    __tablename__ = 'user_profiles'

    ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(255))
    biography = db.Column(db.VARCHAR)
    joined = db.Column(db.String(50))
    photo = db.Column(db.String(100))
    
    
    def __init__(self, first_name, last_name, gender, email, location, biography, joined, photo):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.joined = joined
        self.photo = photo
        