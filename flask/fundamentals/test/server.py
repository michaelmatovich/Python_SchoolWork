from flask import Flask, render_template, redirect
app = Flask(__name__)   


@app.route('/')          
def level_one():
    return render_template("index.html")

@app.route('/gohere')
def level_two():
    print("Yeah man, we totally got to gohere")
    booboo = 4
    return redirect(f"/gohere/{booboo}")

@app.route('/gohere/<int:num>')
def level_three(num):
    print(num)

    return render_template("index2.html", num = num)





if __name__=="__main__":      
    app.run(debug=True)    