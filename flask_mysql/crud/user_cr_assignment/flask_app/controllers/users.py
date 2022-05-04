from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.user import User

@app.route('/')                           
def hello_world():
    return render_template('index.html')  

@app.route('/read')
def read_users():
    users = User.get_all_users()
    print(users)
    return render_template("/read.html", users = users)

@app.route('/create')
def user_form():
    return render_template("/create.html")

@app.route('/create_user', methods = ["POST"])
def create_user():
    data = {'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']    
    }

    User.create_user(data)
    return redirect("/read")

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    # data = {'id': employee_id}
    # Employee.delete_employee(data)
    
    User.delete_user({'user_id': user_id})
    return redirect('/read')

@app.route('/users/<int:user_id>/show')
def show_one_user(user_id):
        
    users = User.get_one_user({'user_id': user_id})
    user = users[0]
    return render_template('/readone.html', user = user)

@app.route('/users/<int:user_id>/edit')
def edit_user_form(user_id):
        
    users = User.get_one_user({'user_id': user_id})
    user = users[0]
    return render_template('/edit.html', user = user, user_id = user_id)

@app.route('/users/<int:user_id>/process', methods = ["POST"])
def edit_user(user_id):
    data = {'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            "user_id": user_id
    }

    User.edit_user(data)
    return redirect("/read")