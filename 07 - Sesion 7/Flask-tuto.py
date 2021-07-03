from flask import Flask

app = Flask(__name__)

# definir una ruta
@app.route("/", methods=['GET', 'POST', 'PUT'])
def home():
    
    #return "Hola mundo"
    return "<html>\
                <body>\
                    <h3><u>Hola mundo</u></h3>\
                </body>\
            </html>"


app.run(debug = True)