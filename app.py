from flask import render_template
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def routePrincipale():
    return render_template("accueil_app.html", titre="Accueil")

@app.route("/date")
def routeDate():
    maintenant = datetime.now().strftime("%d/%m/%Y | %H:%M:%S")
    return render_template("date.html", titre="Date", maintenant=maintenant)

@app.route("/template_base")
def routeTemplateBase():
    return render_template("template_base.html" ,
        titre = "bienvenue sur flask" ,
        mon_titre="Le titre est généré par Python" ,
        mon_paragraphe="Ce paragraphe est aussi généré par Python" ,
        nombre = 12)

@app.route("/main")
def routeMain():
    return render_template("main.html" ,
        titre = "bienvenue sur flask" ,
        mon_titre="Le titre est généré par Python + jinja " ,
        mon_paragraphe="Ce paragraphe est aussi généré par Python + jinja" ,
        nombre = 9 ,
        is_connected=True)

    