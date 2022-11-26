from flask import Blueprint, render_template

from app.db import db
from app.models.rickoso import Rickoso


index_router = Blueprint("index", __name__)

#todo clase sabado
@index_router.route("/")
def index():
    pj = db.rickoso.aggregate([
        {
            "$sort": {"_id": -1}
        },
        {
            "$project": {
                "avatar" : 1,
                "nombre" :1,
                "estado" : 1,
                "especie" : 1,
                "ultimaVez" : 1,
                "primeraVez" : 1
                }
        }
        
    ])
  
    return render_template('index.html',personajes = pj)


