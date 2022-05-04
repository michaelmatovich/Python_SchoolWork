from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User
from flask_app.models.show import Show

@app.route("/new")
def new_show_form():
    if "user_id" not in session:
        return redirect("/")
    
    return render_template("new_show.html")

@app.route("/new/process", methods = ["POST"])
def new_show_process():
    if "user_id" not in session:
        return redirect("/")
    
    if not Show.validate_show(request.form):
        return redirect("/new")
    
    user_id = session["user_id"]

    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "user_id" : user_id
    }
    
    Show.new_show(data)

    return redirect("/dashboard")

@app.route("/dashboard")
def all_tv_shows():
    if "user_id" not in session:
        return redirect("/")

    all_shows = []
    
    data = {"user_id": session["user_id"]}

    user = User.get_by_id(data)
    
    records = Show.get_all_shows()

    for record in records:
        show = Show(record)
        
        user_data = {
            "id": record["users.id"],
            "first_name": record["first_name"],
            "last_name": record["last_name"],
            "email": record["email"],
            "password": record["password"],
            "created_at": record["created_at"],
            "updated_at": record["updated_at"]            
        }

        show.posted_by = User(user_data)

        all_shows.append(show)


    return render_template("dashboard.html", user = user, all_shows = all_shows)

@app.route("/show/<int:show_id>")
def one_tv_show(show_id):
    if "user_id" not in session:
        return redirect("/")

    record = Show.get_one_show({"id": show_id})

    show = Show(record[0])
    
    user_data = {
            "id": record[0]["users.id"],
            "first_name": record[0]["first_name"],
            "last_name": record[0]["last_name"],
            "email": record[0]["email"],
            "password": record[0]["password"],
            "created_at": record[0]["created_at"],
            "updated_at": record[0]["updated_at"]
    }

    show.posted_by = User(user_data)

    return render_template("show_one.html", show = show)

@app.route("/edit/<int:show_id>")
def edit_show_form(show_id):
    if "user_id" not in session:
        return redirect("/")

    record = Show.get_one_show({"id": show_id})

    show = Show(record[0])

    return render_template("edit_show.html", show = show)

@app.route("/edit/<int:show_id>/process", methods = ["POST"])
def edit_show(show_id):
    if "user_id" not in session:
        return redirect("/")

    if not Show.validate_show(request.form):
        return redirect(f"/edit/{show_id}")

    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "id": show_id        
    }

    Show.edit_show(data)
    
    return redirect("/dashboard")

@app.route("/show/delete/<int:show_id>")
def delete_show(show_id):
    if "user_id" not in session:
        return redirect("/")

    Show.delete_show({"id": show_id})


    return redirect("/dashboard")











