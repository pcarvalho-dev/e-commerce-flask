from flask import render_template, session, request, url_for, flash
from market import app, db
from .forms import RegistrationForm

@app.route('/')

def home():
    return "TEST"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
                    #form.password.data)
        #db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title='Register User')

    