from flask import Flask
from users.Users import usersModule

app = Flask(__name__)
app.register_blueprint(usersModule)