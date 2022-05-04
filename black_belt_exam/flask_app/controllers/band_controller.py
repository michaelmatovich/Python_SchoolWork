from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User
from flask_app.models.band import Band

@app.route("/new/sighting")
def new_band_form():
    if "user_id" not in session:
        return redirect("/")
    
    print(session["user_id"])
    data = {"user_id": session["user_id"]}
    print(data)
    user = User.get_by_id(data)
    print(user)
    return render_template("new_band.html", user =user)

@app.route("/new/process", methods = ["POST"])
def new_band_process():
    if "user_id" not in session:
        return redirect("/")
    
    if not Band.validate_band(request.form):
        return redirect("/new/sighting")
    
    user_id = session["user_id"]

    data = {
        "name": request.form["name"],
        "genre": request.form["genre"],
        "city": request.form["city"],
        "user_id" : user_id
    }
    
    Band.new_band(data)

    return redirect("/dashboard")

@app.route("/dashboard")
def all_bands():
    if "user_id" not in session:
        return redirect("/")

    data = {"user_id": session["user_id"]}

    user = User.get_by_id(data)

    all_bands = Band.get_bandmembers(data)

    return render_template("dashboard.html", user = user, all_bands = all_bands)

@app.route("/mybands")
def my_bands():
    if "user_id" not in session:
        return redirect("/")

    data = {"user_id": session["user_id"]}
    
    user = User.get_by_id(data)

    user.get_bands_joined()

    my_bands = Band.get_my_bands(data)

    return render_template("my_bands.html", user = user, my_bands = my_bands)

@app.route("/edit/<int:band_id>")
def edit_band_form(band_id):
    if "user_id" not in session:
        return redirect("/")

    data = {"user_id": session["user_id"]}

    user = User.get_by_id(data)

    band = Band.get_one_band({"id": band_id})

    return render_template("edit_band.html", user = user, band = band)

@app.route("/edit/<int:band_id>/process", methods = ["POST"])
def edit_band(band_id):
    if "user_id" not in session:
        return redirect("/")

    if not Band.validate_band(request.form):
        return redirect(f"/edit/{band_id}")
    
    data = {
        "name": request.form["name"],
        "genre": request.form["genre"],
        "city": request.form["city"],
        "id": band_id        
    }

    Band.edit_band(data)
    
    return redirect("/dashboard")

@app.route("/band/delete/<int:band_id>")
def delete_band(band_id):
    if "user_id" not in session:
        return redirect("/")

    data = {"id": band_id}

    Band.delete_band(data)

    return redirect("/dashboard")

@app.route("/quit/<int:band_id>")
def quit_band(band_id):
    if "user_id" not in session:
        return redirect("/")

    data = {
        "user_id": session["user_id"],
        "band_id": band_id
    }

    User.quit_band(data)

    return redirect("/dashboard")

@app.route("/join/<int:band_id>")
def join_band(band_id):
    if "user_id" not in session:
        return redirect("/")

    data = {
        "user_id": session["user_id"],
        "band_id" : band_id
    }

    User.join_band(data)

    return redirect("/dashboard")












