from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True


def test_username(name):
    if len(name) == 0:
        return "You have not entered any data in this field"
    elif len(name) < 7:
        return "This field must be at least 8 characters"
    else:
        return ""

        

        


@app.route("/signup", methods=['POST'])
def sign_up():
    user_error = ""
    pw_error = ""
    verify_error = ""
    email_error = ""
    username = request.form['user_name']
    pword = request.form['p_word']
    vpassword = request.form['pw_confirm']
    email = request.form['e_email']

    user_error = test_username(username)
    pw_error = test_username(pword)
    
    if len(pword) > 0 and vpassword != pword:
        verify_error = "password doesn't match"




    if user_error or pw_error or verify_error:
        return render_template('uform.html', user_error=user_error, pw_error=pw_error, verify_error=verify_error)




@app.route("/")
def index():
    return render_template('uform.html')

app.run()