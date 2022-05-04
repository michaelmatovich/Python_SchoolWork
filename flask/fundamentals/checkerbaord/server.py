from flask import Flask, render_template  
app = Flask(__name__)   


@app.route('/')          
def level_one():
    return render_template("index.html", x=8, y=8, color1 = "black", color2 = "red")

@app.route('/4')
def level_two():
    return render_template("index.html", x = 4, y = 8, color1 = "black", color2 = "red")

@app.route('/<int:x>/<int:y>')
def level_three(x, y):
    return render_template("index.html", x = x, y = y, color1 = "black", color2 = "red")

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def sensei(x,y,color1,color2):
    return render_template("index.html", x = x, y = y, color1 = color1, color2 = color2)


if __name__=="__main__":      
    app.run(debug=True)    