from flask import Flask, render_template, request, redirect
from datetime import date, datetime

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

if __name__ == '__main__':
    app.run(debug=True)