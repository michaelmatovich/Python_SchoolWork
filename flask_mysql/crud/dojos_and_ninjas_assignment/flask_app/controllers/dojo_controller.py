from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.dojo import Dojo, Ninja

@app.route('/')                           
def hello_world():
    return render_template('index.html')

@app.route('/dojos')
def display_dojos():
    dojos = Dojo.get_all_dojos()
    
    return render_template("/dojos.html", dojos = dojos)

@app.route('/create_dojo', methods = ["POST"])
def create_dojo():
    data = {'name': request.form['name']}

    Dojo.create_dojo(data)

    return redirect("/dojos")

@app.route('/ninjas')
def create_ninja_form():
    dojos = Dojo.get_all_dojos()

    return render_template("ninjas.html", dojos = dojos)

@app.route('/create_ninja', methods = ["POST"])
def create_ninja():
    data = {'dojos_id': request.form['dojos_id'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'age': request.form['age']
    }

    Ninja.create_ninja(data)

    return redirect("/dojos/<int:dojos_id>")

@app.route('/dojos/<int:dojos_id>')
def display_dojo(dojos_id):
    print(dojos_id)

    dojo = Dojo.get_by_id({'dojos_id': dojos_id})
    ninjas = Dojo.get_dojo_ninjas({'dojos_id': dojos_id})
    
    
    return render_template("/display_dojo.html",dojo = dojo, dojos_id = dojos_id, ninjas = ninjas)
