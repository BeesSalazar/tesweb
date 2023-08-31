from flask import Flask 

app = flask("meu app")

@app.route('/')
def hello():
    return "Olá Patinha!"