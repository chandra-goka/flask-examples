from app import app
from flask import render_template

@app.route('/')
def index():
    user_info = {
        'name':'Chandra'
    }
    return render_template('index.html', user=user_info)


@app.route('/profile')
def profile():
    user = {
        'name': 'Chandra'
    }
    profile = {
        'hobbies':['Blogging','Reading Books','Playing chess'],
        'interested_books':{
            'Java':['Thinking in Java','Inside the Java virtual machine'],
            'Python':['Fluent Python']
        }
    }
    return render_template('profile.html', user=user, profile=profile)
