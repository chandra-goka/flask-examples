from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
def index():
    user_info = {
        'name':'Chandra'
    }
    return render_template('index.html', user=user_info)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.user_name.data == 'admin' and form.password.data == 'admin':
            flash('login successful')
            return redirect(url_for('index'))
    return render_template('login.html', form=form)
