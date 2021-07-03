from flask import Flask, render_template

app = Flask(__name__)

# definir una ruta
@app.route("/", methods=['GET', 'POST', 'PUT'])
def home():
    
    #return render_template('index.html')
    return render_template('indexDinamico.html', name = 'Pikachu', tipo = 'Eléctrico') #enviar una variable al template

app.run(debug = True)