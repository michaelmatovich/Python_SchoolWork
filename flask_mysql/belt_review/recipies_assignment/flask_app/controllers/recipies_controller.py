from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def login_successful():
    if "user_id" not in session:
        return redirect("/")
    
    data= {"user_id": session["user_id"]}

    user = User.get_by_id(data)

    user.get_user_recipies(data)

    recipes = Recipe.get_all_recipies(data)

    print("user is")
    print(user)
    print("user recipies is")
    print(user.recipies)
    print("all recipes is")
    print(recipes)
    print(recipes[0])

    
    

    return render_template("dashboard.html", user = user, recipies = recipes)

@app.route('/recipes/new')
def create_recipe_form():
    if "user_id" not in session:
        return redirect("/")

    return render_template("new_recipe.html")

@app.route('/create_recipe', methods = ["POST"])
def create_recipe():
    if "user_id" not in session:
        return redirect("/")

    if not Recipe.validate_recipe(request.form):
        return redirect("/recipes/new")

    user_id = session["user_id"]

    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "is_under_30": request.form["is_under_30"],
        "user_id": user_id
    }

    Recipe.create_recipe(data)

    return redirect("/dashboard")

@app.route("/recipes/<int:id>")
def view_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    print("Heres the id of the recipe")
    print(id)

    recipe = Recipe.get_by_id({"id": id})
    user = User.get_by_id({"user_id": session["user_id"]})

    print("This should be the recipe object")
    print(recipe)
    print(recipe.name)
    print(recipe.is_under_30)
    print(recipe.instruction)
    print(recipe.created_at)

    return render_template("view.html", recipe = recipe, user = user)

@app.route("/recipes/edit/<int:id>")
def edit_recipe_form(id):
    if "user_id" not in session:
        return redirect("/")
    recipe = Recipe.get_by_id({"id": id})

    return render_template("edit_recipe.html", recipe = recipe)

@app.route("/edit_recipe/<int:id>", methods = ["POST"])
def edit_recipe(id):
    if "user_id" not in session:
        return redirect("/")

    user_id = session["user_id"]

    data = {
        "id" : id,
        "name": request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "is_under_30": request.form["is_under_30"]
    }

    Recipe.edit_recipe(data)

    return redirect("/dashboard")



    
