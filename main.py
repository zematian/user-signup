from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            .error {{color: red;}}
        </style>

    </head>
    </body>
    <h1>Signup</h1>
        <form action="/validate" method="POST">
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="">
                        <span class="error">{user_error}</span>
                    </td>
                </tr>

                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password">
                        <span class="error">{password_error}</span>
                    </td>
                </tr>

                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password">
                        <span class="error">{verify_error}</span>
                    </td>
                </tr>

                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" value="">
                        <span class="error">{email_error}</span>
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form>
    </body>
</html>
"""

@app.route('/')
def index():
    return form.format(user_error='' ,password_error='' ,verify_error='' ,email_error='')

def valid_email(Email):

    if len(Email) == 0:
        return True
    elif (len(Email) >= 1 and len(Email) <3) or len(Email) >=20:
        return False
    elif len(Email) >= 3 or len(Email) < 20:
        count_alpha = 0
        count_dot = 0
        for k in Email:
            if k == ' ':
                return False
            elif k == '@':
                count_alpha = count_alpha + 1
            elif k == '.':
                count_dot = count_dot + 1
        if count_alpha ==0 or count_alpha > 1 or count_dot == 0 or count_dot > 1:
            return False
        else:
            return True

@app.route("/validate", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    input_empty_error = ''
    user_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''


    #Username validation
    if len(username) < 3 or len(username) > 20:
        user_error = 'Invalid User Name!'
        username =''

    elif len(username) >= 3 or len(username) < 20:
        for i in username:
            if i == ' ':
                user_error = 'Invalid User Name!'
                username =''

    #Password validation
    if len(password) < 3 or len(password) > 20:
        password_error = 'Invalid Password!'
        password = ''

    elif len(password) >= 3 or len(password) < 20:
        for j in password:
            if j == ' ':
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


    if not input_empty_error and not user_error and not password_error and not verify_error and not email_error:
        return '<h1>Welcome '+ username + '!</h1>'
    else:
        return form.format(user_error=user_error,password_error=password_error, verify_error=verify_error, email_error=email_error)



app.run()

