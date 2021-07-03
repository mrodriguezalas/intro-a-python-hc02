from flask import Flask, render_template

app = Flask(__name__)

# definir una ruta
@app.route("/", methods=['GET', 'POST', 'PUT'])
def home():
    
    return render_template('indexWithStyle.html', name = 'Mew', tipo = 'Psych') #enviar una variable al template

app.run(debug = True)