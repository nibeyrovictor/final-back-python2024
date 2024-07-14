from flask import Flask, render_template, request, redirect
from datetime import date, datetime

from controller_db import *


app = Flask(__name__)

def basicInfo(getTitle):
    #Día actual
    today = date.today()
    #Fecha actual
    now = datetime.now()
    # Seccion
    title = getTitle
    return [title, today.strftime('%Y'), now]

@app.route("/")
def home():
    title="Home"
    # return saludo
    return render_template("index.html",title=basicInfo(title))


@app.route("/contacto")
def contacto():
    title="Contactos"
    return render_template("contacto.html",title=basicInfo(title))

@app.route("/contacto_carga", methods=['POST'])
def cargar_formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        comentario = request.form['comentario']
        mail = request.form['mail']
        
        # Call the function to save the data
        result = guardar_contacto(nombre, apellido, comentario, mail)
        
        if result:  # Check if the insert was successful
            print("Data saved successfully!")
        else:
            print("Error saving data.")
        
        return redirect("/")  # Redirect back to home or another page

   # Call the contacto function to save data
    result = contacto(nombre, apellido, comentario, mail)
    print(result)  # Optional: Log the result to the console
    
    return redirect("/")  # Redirect to the home page after submission

if __name__ == "__main__":
    app.run(debug=True)