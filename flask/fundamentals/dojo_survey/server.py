from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'booboo'                  



@app.route('/')                           
def dojo_survey():
    return render_template('index.html')
    
@app.route('/process', methods = ['POST'])
def process_survey():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['fav_language'] = request.form['fav_language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def show_survey():
    return render_template('result.html')






if __name__=="__main__":
    app.run(debug=True)  