from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.models import UserProfile
from flask import session
from app.forms import profileForm
from datetime import date


###
# Routing for your application.
###

#Render home page
@app.route('/')
def home():
    return render_template('home.html')

#Render about page   
@app.route('/about/')
def about():
    return render_template('about.html')

#Render add profile page    
@app.route('/profile/', methods = ["GET", "POST"])
def profile():
    form = profileForm()
    
    if request.method == "POST" and form.validate_on_submit():
        #collect from data
        fname = form.firstName.data
        lname = form.lastName.data
        gender = form.gender.data
        email = form.email.data
        location = form.location.data
        bio = form.biography.data
        date_joined = str(date.today())
       
        #connect to database and save data
        user_profile = UserProfile(fname, lname, gender, email, location, bio, date_joined)
        db.session.add(user_profile)
        db.session.commit()
        
        flash("Your profile has been sucessfully added!", "success")
        return redirect(url_for('profiles'))
        
    return render_template('add_profile.html', form=form)

#Render page that displays all user    
@app.route('/profiles/')
def profiles():
    
    #connect to database and fectch user profiles
    users = UserProfile.query.order_by(UserProfile.first_name).all()
    return render_template('profiles.html', users=users)

#Render page that displays a single user page using user ID   
@app.route('/profile/<userid>', methods=["POST"])
def view_profile(userid):
    
    #connect to database and fectch user profile
    user = UserProfile.query.filter_by(user_id='userid').first()
    return render_template('profile.html', user=user)

#####_______________________________________________________________________________________________#####

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


# @app.errorhandler(404)
# def page_not_found(error):
#     """Custom 404 page."""
#     return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
