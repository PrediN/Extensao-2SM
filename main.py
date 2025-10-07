from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask('validacao')
app.config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Senai%40134@127.0.0.1/db_validacao'
