from flask import render_template, Flask

application = Flask(__name__)

@application.route('/inicio')
def inicio():
    return render_template('inicio.html')

if __name__ == '__main__':
    application.run(debug=ON, host = '127.0.0.1')
    
