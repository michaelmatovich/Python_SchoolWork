# Virtual Environment Commands
#Start
pipenv install flask==2.0.3
pipenv shell
#End
Ctrl + C
Exit
------------------------------------------------------------
#Server.py Template
from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def hello_world():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html')  
    
if __name__=="__main__":
    app.run(debug=True)  
------------------------------------------------------------
#Sever.py Template for POST requests
from flask import Flask, render_template, request, redirect # added request
            
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')

------------------------------------------------------------
#Server.py Template for Session
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

---------------------------------------------------------------------------


#Static link
<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/my_style.css') }}">
<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='js/my_script.js') }}"></script>
<!-- linking an image -->
<img src="{{ url_for('static', filename='img/my_img.png') }}">