#from werkzeug.urls import url_parse #* para la pass (hash) encriptada
from app import create_app
#from app.forms import LoginForm, PostForm,CommentForm
from app.db import db


app = create_app()



if __name__ == "__main__":
    app.run()

