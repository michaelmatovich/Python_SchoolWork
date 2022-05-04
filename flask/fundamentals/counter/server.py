from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'booboo'                  



@app.route('/')                           
def counter():
    if 'visits' in session:
        session['visits'] += 1    
    else:
        session['visits'] = 1
    return render_template('index.html', visits = session['visits'])
    
@app.route('/destroy_session')
def reset():
    session['visits'] = 0
    return redirect('/')















if __name__=="__main__":
    app.run(debug=True)  