from flask import Flask, request, redirect, render_template
import cgi
import os
import re

EMAIL_REGEX = re.compile('[a-zA-Z0-9._%+-]{3,20}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}')

app = Flask(__name__)
app.config['DEBUG'] = True



def test_username(name):
    for a in name:
        if a == " ":
            return "Spaces are not valid characters."
    if len(name) == 0:
        return "You have not entered any data in this field"
    elif len(name) < 3 or len(name) > 20:
        return "This field must be between 3 and 20 characters"
    else:
        return ""

def test_useremail(name):
    if not name:
        return ""
    for a in name:
        if a == " ":
            return "Spaces are not valid characters in email."
    if not EMAIL_REGEX.match(name):
        return "Invalid. email must be 3-20 characters with a @ and . "


        


@app.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        user_error = ""
        pw_error = ""
        verify_error = "" 
        username = request.form['user_name']
        print(username)
        pword = request.form['p_word']
        vpassword = request.form['pw_confirm']
        email = request.form['e_email']

        user_error = test_username(username)
        print(username)
        pw_error = test_username(pword)
        email_error = test_useremail(email)
        
        if len(pword) > 0 and vpassword != pword:
            verify_error = "verification password doesn't match"




        if user_error or pw_error or verify_error or email_error:
            print(username)
            return render_template('uform.html', user_name=username, e_email=email, user_error=user_error, pw_error=pw_error,verify_error=verify_error, email_error=email_error)
        else:

            return redirect('/welcome?success={0}'.format(username))
        
    else:
        return render_template("uform.html")


@app.route('/welcome')
def welcome():
    success = request.args.get('success')
    return render_template('signup.html', success=success )

@app.route("/")
def index():
        return redirect("/signup")

app.run()