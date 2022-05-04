from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():

    return render_template("index.html")

# VALIDATE

@app.route("/register", methods = ["POST"])
def register_user():
    
    if not User.validate_register(request.form):
        return redirect("/")
    # pw = request.form["password"]
    # print(pw)
    password_hash = bcrypt.generate_password_hash(request.form["password"])
    
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": password_hash
    }

    user_id = User.register_user(data)

    session["user_id"] = user_id

    return redirect("/success")


@app.route('/login', methods=['POST'])
def login_user():
    
    data = {"email" : request.form["email"]}
    
    pw = request.form["password"]
    print(pw)
    user_in_db = User.get_by_email(data)
    
    if not user_in_db:
        flash("Invalid Email or Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid Email or Password")
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    
    return redirect("/success")

@app.route('/success')
def login_successful():
    if "user_id" not in session:
        return redirect("/")
    data = {"user_id": session["user_id"]}

    users = User.get_by_id(data)
    # print("Here is users")
    # print(users)
    user = users[0]
    # print("Here is user")
    # print(user)

    print(user["first_name"])
    return render_template("success.html", user = user)

@app.route('/logout')
def logout_sucessful():
    session.clear()
    return render_template("logout.html")
