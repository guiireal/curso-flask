from flask import Flask
from src.routes.routes import *

app = Flask(__name__)


app.add_url_rule(routes['product']['index']['route'], view_func=routes['product']['index']['controller'])
app.add_url_rule(routes['product']['destroy']['route'], view_func=routes['product']['destroy']['controller'])
app.add_url_rule(routes['product']['edit']['route'], view_func=routes['product']['edit']['controller'])
app.add_url_rule(routes['product']['update']['route'], view_func=routes['product']['update']['controller'])

@app.errorhandler(404)
def not_found(_):
  return "Página não encontrada!"