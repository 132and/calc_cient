from flask import render_template, Flask

application = Flask(__name__)

@application.route('/inicio')
def inicio():
    return render_template('main.html')
    
