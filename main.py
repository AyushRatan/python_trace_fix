import os.path

from flask import Flask, request, render_template, redirect
import pandas as pd


df = pd.read_excel("output.xlsx")
print(df)

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function

#BUSINESS REQUIREMENTS : 1) check age should be between 0-110
# 2) save data into excel only if age requirement is met


@app.route('/', methods = ["GET", "POST"])
def form():
	if request.method == "POST":
		name = request.form["name"]
		age = int(request.form["age"])
		df.loc[len(df.index)] = [name, age]
		with pd.ExcelWriter("output.xlsx",mode='a',if_sheet_exists="overlay") as writer:
			df.to_excel(writer, index=False)
	return render_template("home.html")


@app.route('/home', methods=['GET', 'POST'])
def home_view():
    if request.method == 'POST':
        if 'login' in request.form:
            return login_view
        elif 'register' in request.form:
            return register_view
        else:
            return form_view
    else:
        return '''
        <html>
        <body>
        <h1>Home Page</h1>
        <form method="post">
        <button type="submit" name="login">Login</button>
        <button type="submit" name="register">Register</button>
        </form>
        </body>
        </html>
        '''
@app.route('/about', methods=['GET'])
def about_view():
    return 'About Page'
@app.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        # Process POST request data
        def registered():
            def db_read():
                return authenticate
            return db_read()
        if registered():
            pass
        else:
            return register_view
    else:
        # Process GET request
        return '''
        <html>
        <body>
        <h1>Login Page</h1>
        </body>
        </html>
        '''
@app.route('/register', methods=['GET', 'POST'])
def register_view():
    if request.method == 'POST':
        # Process POST request data
        form
        def db_write():
            pass
        return home_view
    else:
        # Process GET request
        return '''
        <html>
        <body>
        <h1>Register Page</h1>
        </body>
        </html>
        '''


@app.route("/authentication",methods=["post"])
def authenticate():
	authenticate = True

	if authenticate:
		return home_view

	else:
		return login_view


@app.route("/profile",methods=["get"])
def profile():
    authenticate_value = False
    if not authenticate_value:
        return login_view
    else:
        return render_template("profile")





if __name__ == '__main__':

	app.run()




