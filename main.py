from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    user_error=''
    password_error=''
    verify_error=''
    email_error=''
    return render_template('index.html')

#@app.route("/")
#def index():
    #return form.format(user_error='' ,password_error='' ,verify_error='' ,email_error='')

def valid_email(Email):

    if len(Email) == 0:
        return True
    elif (len(Email) >= 1 and len(Email) <3) or len(Email) >=20:
        return False
    elif len(Email) >= 3 or len(Email) < 20:
        count_alpha = 0
        count_dot = 0
        for i in Email:
            if i == ' ':
                return False
            elif i == '@':
                count_alpha = count_alpha + 1
            elif i == '.':
                count_dot = count_dot + 1
        if count_alpha ==0 or count_alpha > 1 or count_dot == 0 or count_dot > 1:
            return False
        else:
            return True

@app.route("/validate", methods=['GET', 'POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    #input_empty_error = ''
    user_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''


    #Username validation
    if len(username) < 3 or len(username) > 20:
        user_error = 'Invalid User Name!'
        username =''

    elif len(username) >= 3 or len(username) < 20:
        for j in username:
            if j == ' ':
                user_error = 'Invalid User Name!'
                username =''
    
    #Password validation
    if len(password) < 3 or len(password) > 20:
        password_error = 'Invalid Password!'
        password = ''

    elif len(password) >= 3 or len(password) < 20:
        for k in password:
            if k == ' ':
                password_error = 'Invalid Password!'
                password = ''

    #Password verification 
    if password != verify:
        verify_error = 'Password not matching!'
        verify = ''

    #Email validation
    if not valid_email(email):
        email_error = 'Invalid Email!' 
        email = ''


    if not user_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('index.html', user_error=user_error, password_error=password_error, verify_error=verify_error, email_error=email_error)
        
@app.route('/welcome')
def welcome():
    username = request.args.get('username') 
    return render_template('welcome.html',username=username)
    #return '<h1>Welcome, {0}!</h1>'.format(username)

app.run()

