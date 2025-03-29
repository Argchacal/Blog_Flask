from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient
import os#se importa os para poder acceder a la informacion del.env 
from dotenv import load_dotenv


def crear_app():
    app= Flask(__name__)
    entradas =[]
    cliente = MongoClient(os.getenv("MONGODB_URI"))
    app.db = cliente.Blog 
    entradas =[entrada for entrada in app.db.Entrada_contenido.find({})
    ]
    @app.route(rule="/", methods = ["GET", "POST"])
    def home():
        if request.method == "POST":
            titulo = request.form.get("tit")#toma informacion del imput del html y lo pasa a una variable
            contenido_entrante = request.form.get("Contenido")
            fecha_formato = datetime.datetime.today().strftime("%d-%m-%y")#toma la fecha actual y con el strftime(" %d-%m-%y ") le asignamos
            parametros = {"titulo": titulo, "contenido": contenido_entrante, "fecha":fecha_formato}#creo una diccionario con la informacion obtenida
            app.db.Entrada_contenido.insert_one(parametros)
        return render_template( template_name_or_list = "index.html", entrada = entradas) # envio al html la informacion de las entradas actuales

    return app
if __name__ == "__main__":
    app= crear_app()
    app.run()